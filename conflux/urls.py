def build_page_url(url: str, page : int, limit : int = 100) -> str:
    if "?" in url:
        return f"{url}&limit={limit}&page={page}"
    else:
        return f"{url}?limit={limit}&page={page}"