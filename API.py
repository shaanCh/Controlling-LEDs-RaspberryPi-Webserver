#Using Postman Web Api to create code snipet requests for Spotify API
#https://web.postman.co/workspace/My-Workspace~fb306756-5e0a-4fa0-8c53-6c32df7a4f16/request/26533462-50871f04-4144-48d4-ad70-f3017af37e4a?ctx=code


import os
import requests

url = "https://api.spotify.com/v1/search?q=Travis%20Scott&type=artist"



payload={}
headers = {
  'Authorization': 'BQCUruHZ66m7HpjkCn-nTteqgDPoAmI2fUPAJaGHW0KdCfGx3qbSi5RxQgvEJBwSjf9gqB2WA2rN1V0XRZzflBa-dHwYqT5Rjoi0WDMF03PlN4SxiYotT9FPtE7jP_qkcSTEEcfBZzJAA2AitHYN1wxeph7Kr1O6ocd3iYUR9z0ukrdQma5LUurXZLDbsNy5PgqU'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
