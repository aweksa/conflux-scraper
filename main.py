from conflux.pagination import iterate_pages

SITE_URL = "https://conflux.rx/Board-Games"

def main():
    for page_num, html in iterate_pages(SITE_URL):
        print(f"Fetched page {page_num}")
    
if __name__ == "__main__":
    main()



    

    

        