import requests
from .connfig import HEADERS
from typing import Optional

def fetch_page(url : str, timeout: int = 15) -> Optional[str]:
    try:
        resp = requests.get(url, headers=HEADERS, timeout=timeout)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(f"[fetch error] {url} -> {e}")
        return None