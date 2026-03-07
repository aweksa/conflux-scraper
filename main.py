from conflux.pagination import iterate_pages
from conflux.parsing import parse_products
from conflux.fetching import fetch_page
from conflux.database import initialize_db, connect
import sqlite3

SITE_URL = "https://conflux.rs/Board-Games"
TEST_URL = "https://conflux.rs/Board-Games?limit=100"

def main():
    initialize_db()

    conn = connect()
    cursor = conn.cursor()

    for page_num, html in iterate_pages(SITE_URL):
        print(f"Fetched page {page_num}")
        products = parse_products(html)

        for p in products:
            cursor.execute(
                "INSERT OR IGNORE INTO products (product_id, title, link) VALUES (?, ?, ?)", (p["product_id"], p["title"], p["link"])
            )

            if p["price"] is not None:
                cursor.execute(
                    "INSERT INTO price_history (product_id, price) VALUES (?, ?)", (p["product_id"], p["price"])
                )
            
            cursor.execute(
                "INSERT INTO stock_history (product_id, status, quantity, arrival_date) VALUES (?, ?, ?, ?)", (p["product_id"], p["status"], p["quantity"], p["arrival_date"])
            )
            conn.commit()

    conn.close()
if __name__ == "__main__":
    main()


        