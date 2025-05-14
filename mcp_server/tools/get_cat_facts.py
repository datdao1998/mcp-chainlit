import requests

def get_facts() -> str:
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    if (response.status_code == 200):
        return response.json()['fact']
    
    return "Cannot generate random fact about cats."