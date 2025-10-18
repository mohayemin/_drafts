import aiohttp

API_ROOT = "https://api.example.com/"
HEADERS = {
    "User-Agent": "my-app/0.0.1"
}

async def fetch_data(url, params):
  api_url = API_ROOT + url
  async with aiohttp.ClientSession() as ses:
    async with ses.get(api_url, params=params,
                       headers = HEADERS) as r:
      if r.status != 200: 
        raise Exception("error fetching")

      return await r.json()
