import re
url = "https://example.com/path/to/resource"
url_regex = r"https://example\.com/path/to/(\w+)"
import aiohttp
from bs4 import BeautifulSoup


























if re.search(url_regex, url):
  result = url_regex.search(url)
  url = result.group(0)

async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
        page = await response.text()

soup = BeautifulSoup(page, 'html.parser')
