import re
from urllib.parse import urlparse

def extract_features(url):
    parsed = urlparse(url)

    url_length = len(url)
    hostname_length = len(parsed.netloc)
    num_dots = url.count('.')
    num_hyphens = url.count('-')
    num_digits = sum(c.isdigit() for c in url)
    has_https = 1 if parsed.scheme == "https" else 0
    has_ip = 1 if re.match(r"\d+\.\d+\.\d+\.\d+", parsed.netloc) else 0
    num_special_chars = len(re.findall(r'[@?&=_%]', url))

    return [
        url_length,
        hostname_length,
        num_dots,
        num_hyphens,
        num_digits,
        has_https,
        has_ip,
        num_special_chars
    ]