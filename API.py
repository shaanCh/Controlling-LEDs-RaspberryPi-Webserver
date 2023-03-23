import requests

url = "https://api.spotify.com/v1/search?q=Travis%20Scott&type=artist"

payload={}
headers = {
  'Authorization': 'Bearer BQB2AYxIN7-whoLRNb9p2gABPwgMiCwGn5NoHHV8S8ArdUSEAlSII7G50TX5Zkx9A13kM0T60pcTYluWurDb2O9BSGHtMiJ0U38T0uEAS6mN7-61IykGNx_FwVc-e2Os3LlqSVmqsfWN3RySjWZNvJyXWgvdm6P2ZugPA3qcJ1v1kBF2TUya0LjXGzRnvcWU5wjP'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
