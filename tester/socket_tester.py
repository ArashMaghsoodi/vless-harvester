import socket
from urllib.parse import urlparse
from config import TIMEOUT

def is_server_reachable(vless_url):
    try:
        parsed = urlparse(vless_url)
        with socket.create_connection((parsed.hostname, parsed.port), timeout=TIMEOUT):
            return True
    except:
        return False