from bs4 import BeautifulSoup

def parse_product(html: str) -> list[dict]:
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

            stock_container = container.select_one("span.stat-2")

            products.append({"product_id" : product_id,
            "title" : title,
            "price" : price,
            "link" : link,})

        except Exception as e:
            print(f"Error parsing product: {e}")

    return products
