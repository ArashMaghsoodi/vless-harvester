import requests, re
from config import USER_AGENT

def fetch_vless_links():
    url = "https://www.vpnjantit.com/free-v2ray-vless"
    r = requests.get(url, headers={"User-Agent": USER_AGENT})
    return set(re.findall(r'vless://[^\s"\'<>]+', r.text))