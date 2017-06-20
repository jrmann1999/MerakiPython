import requests, json

apikey = 'XXXX'
headers = {'X-Cisco-Meraki-API-Key': apikey, 'Content-Type': 'application/json'}
parameters = {'name': 'SSID'}

url = 'https://dashboard.meraki.com/api/v0/organizations'

r = requests.get(url, headers=headers)
if (r.ok):
 orgid = r.json()[0]['id']

url = 'https://dashboard.meraki.com/api/v0/organizations/' + str(orgid) + '/networks'

r = requests.get(url, headers=headers)
if (r.ok):
 for network in r.json():
  if (network['type'] == 'combined' or network['type'] == 'wireless'):
   url = 'https://dashboard.meraki.com/api/v0/networks/' + str(network['id']) + '/ssids'
   r2 = requests.get(url, headers=headers)
   if (r2.ok):
     for ssid in r2.json():
      if ssid['name'] == 'SSID':
        url2 = 'https://dashboard.meraki.com/api/v0/networks/' + str(network['id']) + '/ssids/' + str(ssid['number'])
        r3 = requests.put(url2, headers=headers, data=json.dumps(parameters))
        print url2, r3.status_code        
