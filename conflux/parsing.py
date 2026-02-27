from bs4 import BeautifulSoup
from datetime import datetime
import re
def parse_products(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "lxml")
    products = []
    containers = soup.select("div.product-layout")

    for container in containers:
        try:
            product_id = container.get("data-product-id")

            name_tag = container.select_one("div.name a")
            title = name_tag.get_text(strip=True)
            link = name_tag["href"]

            price_tag = container.select_one("span.price-normal")
            price = price_tag.get_text(strip=True) if price_tag else None
            price = re.sub(r"[^\d.]", "", price)
            price = price.split(".")[0]
            if price:
                price = int(price)
            else:
                price = None

            status = "unknown"
            quantity = None
            arrival_date = None

            arrival_label = container.select_one("span.product-label-364")

            if container.select_one("span.product-label-30"):
                label_text = container.select_one("span.product-label-30").get_text(strip=True).lower()
                if "stanju" in label_text:
                    status = "out_of_stock"       
                    quantity = 0     
            
            elif arrival_label:
                text = arrival_label.get_text(strip=True)
                if text.lower().startswith("stize oko"):
                    text = text[9:].strip()
                try:
                    arrival_date = datetime.strptime(text, "%d.%m.%Y").date()
                except ValueError:
                    arrival_date = None
                status = "incoming"
                quantity = 0
            

            
            else:
                stock_container = container.select_one("span.stat-2 span:last-child")
                if stock_container:
                    text = stock_container.get_text(strip=True)
                    if text.isdigit():
                        quantity = int(text)
                        status = "in_stock"
                        

            products.append({"product_id" : product_id,
            "title" : title,
            "price" : price,
            "link" : link,
            "status" : status,
            "quantity" : quantity,
            "arrival_date" : arrival_date,})

        except Exception as e:
            print(f"Error parsing product: {e}")

    return products
