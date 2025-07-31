from urllib.parse import urlparse, parse_qs

def parse_vless_url(url):
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    return {
        "uuid": parsed.username,
        "host": parsed.hostname,
        "port": parsed.port,
        "params": {k: v[0] for k, v in params.items()}
    }