import requests, bs4, pyperclip
print("Searching for laptops.....")
print("-" * 25)
url = pyperclip.paste()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
product_cards = soup.find_all("div", {"class" : "puis-card-container"})
with open("laptop_prices.txt", "w", encoding="utf-8") as file:
    file.write("----- Amazon Laptop Prices ------\n\n")

    count = 0
    for card in product_cards:
        if count >= 20:
            break

        h2_element = card.find("h2")
        price_element = card.find("span", {"class" : "a-price-whole"})

        if h2_element and price_element:
            span_element = h2_element.find("span")
            if span_element:
                laptop_title = span_element.text.strip()
            else:
                laptop_title = h2_element.text.strip()
            laptop_price = price_element.text.strip()

            count += 1

            output = f"{count}. {laptop_title[:50]}  | Price: {laptop_price}ج\n"
            file.write(output)
    print("Done! check the file")