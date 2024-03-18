# Python Programme Number 68
# Slicing example for Python
# Programmer: Mukul Dharwadkar
# Date: 6th December 2006

# This programme will slice a URL to extract the domain name from the URL

url = raw_input("Please enter the URL: ")
domain = url[11:-4]

print "Domain name: " , domain
