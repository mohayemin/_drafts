import requests

API_ROOT = "https://api.example.com/"
HEADERS = {
    "User-Agent": "my-app/0.0.1"
}

def fetch_data(url, params):
  api_url = API_ROOT + url
  r = requests.get(api_url, params=params, 
                   headers=HEADERS)

  if r.status_code != 200:
        raise Exception("error fetching")

  return r.json()
