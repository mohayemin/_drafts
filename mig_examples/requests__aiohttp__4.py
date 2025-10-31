import re
url = "https://example.com/path/to/resource"
regex = r"https://example\.com/path/to/(\w+)"
import requests
from bs4 import BeautifulSoup

























if re.search(regex, url):
  result = regex.search(url)
  url = result.group(0)

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
