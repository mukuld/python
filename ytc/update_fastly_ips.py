import boto3
import json
import urllib3

def lambda_handler(event, context):
    # Get Fastly IPs
    url = "https://api.fastly.com/public-ip-list"
    http = urllib3.PoolManager()
    response = http.request('GET', url)
   
    ipv4 = []
    ipv6 = []
    if response.status == 200:
        data = response.data.decode('utf-8')
        json_data = json.loads(data)
        ipv4.append(json_data["addresses"])
        ipv6.append(json_data["ipv6_addresses"])
    else:
        raise Exception(f"Request failed with status code: {response.status}")


    # Update security group inbound rules
    update_security_group_rules(ipv4, ipv6)
    
    if update_security_group_rules(ipv4, ipv6):
        return {
            'statusCode': 200,
            'body': 'Successfully updated security group rules'
        }
    else:
        # Handle potential errors during update
        return {
            'statusCode': 500,
            'body': 'Failed to update security group rules'
        }


def update_security_group_rules(ipv4, ipv6):
    ec2_client = boto3.client('ec2')

    security_group_ids = ["sg-0e12f7c21e42e82b3"]

    for security_group_id in security_group_ids:
        # Get current inbound rules
        current_rules_response = ec2_client.describe_security_groups(GroupIds=[security_group_id])
        current_rules = current_rules_response["SecurityGroups"][0]["IpPermissions"]
        # Update inbound rules to allow access from Fastly IPs
        updated_rules = []
        revoke_rules = []
        for rule in current_rules:
            if (rule.get('FromPort') == 80 and rule.get("ToPort") == 80) or (rule.get("FromPort") == 443 and rule.get("ToPort") == 443):  # Don't modify non-HTTP rules
                revoke_rules.append(rule)
                continue
       
        fastly_ips = list(map(lambda x: {'CidrIp': x, 'Description': 'Fastly IP'}, ipv4[0]))
        fastly_ipv6s = list(map(lambda x: {'CidrIpv6': x, 'Description': "Fastly IPv6"}, ipv6[0]))
        # Allow access from Fastly IPs for HTTP traffic
        updated_rules.append({
            "FromPort": 80,
            "ToPort": 80,
            "IpProtocol": "tcp",
            "IpRanges": fastly_ips,
            "UserIdGroupPairs": [],
        })
         # Allow access from Fastly IPs for HTTPS traffic
        updated_rules.append({
            "FromPort": 443,
            "ToPort": 443,
            "IpProtocol": "tcp",
            "IpRanges": fastly_ips,
            "UserIdGroupPairs": [],
        })
        # Allow access from Fastly IPs for HTTP traffic
        updated_rules.append({
            "FromPort": 80,
            "ToPort": 80,
            "IpProtocol": "tcp",
            "Ipv6Ranges": fastly_ipv6s,
            "UserIdGroupPairs": [],
        })
         # Allow access from Fastly IPs for HTTPS traffic
        updated_rules.append({
            "FromPort": 443,
            "ToPort": 443,
            "IpProtocol": "tcp",
            "Ipv6Ranges": fastly_ipv6s,
            "UserIdGroupPairs": [],
        })
        
        # Apply the updated rules
        ec2_client.revoke_security_group_ingress(GroupId=security_group_id, IpPermissions=revoke_rules)
        ec2_client.authorize_security_group_ingress(GroupId=security_group_id, IpPermissions=updated_rules)

        return {
            "Success"
        }