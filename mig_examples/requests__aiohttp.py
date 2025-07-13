import requests

url = "..."
headers = {...}

r = requests.get(url, headers)
if r.status_code != 200:
  raise Exception("error getting info")

result = r.json()
quota = result["account_quota"]
quota_used = result["quota_used"]
