# documentation
# https://support.appsflyer.com/hc/en-us/articles/360001250345-OneLink-API#create-onelink-attribution-link

# imports
import http.client
import mimetypes
import json

# variables
api_key = '' #manditory, see here how to retrieve: https://support.appsflyer.com/hc/en-us/articles/360001250345-OneLink-API#authentication-key%C2%A0
onelink_id = '' #manditory, use a OneLink ID which is created in the AppsFlyer dashboard.
body = {
    # "brand_domain": "click.example.com", #optional, requires a configured branded link
    "ttl" : "25", #optional, default is 31d
    "data" : {
        "pid" : "SMS-Offer",
        "c" : "Coupon",
        "custom_param" : "value"
    }
}

# code - no need to edit
conn = http.client.HTTPSConnection("onelink.appsflyer.com")
payload = json.dumps(body)
headers = {
		'Content-Type': 'application/json',
		'authorization': api_key
}
conn.request("POST", "/shortlink/v1/" + onelink_id, payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))