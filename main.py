import requests
from typing import Optional, Iterator, Tuple
from bs4 import BeautifulSoup
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}

def fetch_page(url : str, timeout: int = 15) -> Optional[str]:
    try:
        resp = requests.get(url, headers=HEADERS, timeout=timeout)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(f"[fetch error] {url} -> {e}")
        return None
    
def build_page_url(url: str, page : int, limit : int = 100) -> str:
    if "?" in url:
        return f"{url}&limit={limit}&page={page}"
    else:
        return f"{url}?limit={limit}&page={page}"
    
def page_has_product(html: str) -> bool:
    soup = BeautifulSoup(html, "lxml")
    return bool(soup.select(".product-layout"))

def iterate_pages(url : str, delay : float = 0.5) -> Iterator[Tuple[int, str]]:
    page = 1
    while True:
        url = build_page_url(url, page)
        html = fetch_page(url)
        if not html:
            break
        
        if not page_has_product(html):
            break
        
        yield page, html
        
        page += 1
        
        time.sleep(delay)
        