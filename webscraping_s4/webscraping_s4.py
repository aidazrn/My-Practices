import requests
import bs4

response = requests.get("https://torob.com/search/?query=%D8%A7%DB%8C%D8%B1%D9%BE%D8%A7%D8%AF")
print(response)


soup = bs4.BeautifulSoup(response.text, "html.parser")

name = soup.find_all("h2", attrs={"class" : "ProductCard_desktop_product-name__JwqeK"})
price = soup.find_all("div", attrs={"class" : "ProductCard_desktop_product-price-text__y20OV"})


for n in name:
    print(n.text)

print(20 * "-")

for p in price:
    print(p.text)