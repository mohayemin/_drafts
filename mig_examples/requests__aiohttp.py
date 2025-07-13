import aiohttp

url = "..."
headers = {...}

async with aiohttp.ClientSession() as ses:
  async with ses.get(url, headers) as r:
    if r.status != 200:
      raise Exception("error getting info")
    
    result = await r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    