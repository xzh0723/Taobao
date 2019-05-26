import requests
from utils.config import *

def get_random_proxy():

    res = requests.get(proxy_url)
    result = res.json()
    ip = result['data'][0]['ip']
    port = result['data'][0]['port']
    proxy = f'{ip}:{port}'
    print(proxy)
    proxies = {
        'http': f'http//{proxy}',
        'https': f'https://{proxy}'
    }
    return proxies


