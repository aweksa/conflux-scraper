from conflux.pagination import iterate_pages
from conflux.parsing import parse_products
from conflux.fetching import fetch_page
import pandas as pd
SITE_URL = "https://conflux.rs/Board-Games"
TEST_URL = "https://conflux.rs/Board-Games?limit=100"

def main():
    for page_num, html in iterate_pages(SITE_URL):
        print(f"Fetched page {page_num}")
    
if __name__ == "__main__":
    main()


        