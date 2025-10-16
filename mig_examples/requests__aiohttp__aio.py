import aiohttp

async def fetch_data(url, params):
    api_url = API_ROOT + url
    async with aiohttp.ClientSession() as ses:
        async with ses.get(api_url, params=params) as r:
            if r.status == 200: 
                return await r.json()
        raise Exception("error fetching")
    