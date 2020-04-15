import requests

def handler(event, context):
    r = requests.get("http://www.dharwadkar.com")
    print(r.text[0:500])
    if r.status_code == 200:
        return "Success!"
    else:
        return "FAILURE!"
