import requests

def fetch_data(url, params):
    api_url = API_ROOT + url
    r = requests.get(api_url, params=params)
    
    if r.status_code != 200:
        raise Exception("error fetching")
    
    return r.json()
