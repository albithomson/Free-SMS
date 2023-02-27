
import requests

servicePlanId = "add service plan id"
apiToken = "add api token"
sinchNumber = "add sinch no"
toNumber = "add phn no"
url = "https://us.sms.api.sinch.com/xms/v1/" + servicePlanId + "/batches"

payload = {
  "from": sinchNumber,
  "to": [
    toNumber
  ],
  "body": "Hello how are you"
}

headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer " + apiToken
}

response = requests.post(url, json=payload, headers=headers)

data = response.json()
print(data)