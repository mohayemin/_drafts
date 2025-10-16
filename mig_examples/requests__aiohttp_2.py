import requests
if re.search(regex, url):
  result = regex.search(url)
  url = result.group(0)

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
