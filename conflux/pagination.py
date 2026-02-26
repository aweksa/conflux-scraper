from bs4 import BeautifulSoup
from typing import Iterator, Tuple
from .fetching import fetch_page
from .urls import build_page_url
import time

def page_has_product(html: str) -> bool:
    soup = BeautifulSoup(html, "lxml")
    return bool(soup.select(".product-layout"))

def iterate_pages(url : str, delay : float = 0.01) -> Iterator[Tuple[int, str]]:
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