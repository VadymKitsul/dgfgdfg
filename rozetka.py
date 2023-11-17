import requests
from bs4 import BeautifulSoup
import lxml



user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
headers = {"User-Agent": user}

sessions = requests.Session()
for i in range(1, 7):
    url = f"https://cash-backer.club/shops?page={i}"
    response = sessions.get(url, headers=headers)
    # print(response.status_code)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        # print(soup)
        products = soup.find_all("div", class_="col-lg-2 col-md-3 shop-list-card pseudo-link no-link")
        #print(products[0])

        for prod in products:
            if prod.find('div', class_="card-body"):
                title = prod.find("div", class_="shop-title")
                cashback = prod.find("div", class_="shop-rate")
                print('Product: ', title.text.strip(), 'cashback: ', cashback.text)
                with open("catalog.txt", "a", encoding='utf-8') as file:
                    file.write(f"{title.text} {cashback.text}\n")