import requests
from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()
headers["Connection"] = "keep-alive"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
headers["Upgrade-Insecure-Requests"] = "1"
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headers["Accept-Language"] = "en-US,en;q=0.9"
headers["Accept-Encoding"] = "gzip, deflate"

