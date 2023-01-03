import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://2gis.kg/bishkek/search/%D1%87%D0%B0%D1%81%D1%82%D0%BD%D1%8B%D0%B5%20%D0%BA%D0%BB%D0%B8%D0%BD%D0%B8%D0%BA%D0%B8%20%D0%B2%20%D0%B1%D0%B8%D1%88%D0%BA%D0%B5%D0%BA%D0%B5/page/p1")
html = BS(r.text, "html.parser")

for el in html.select("._awwm2v > ._1hf7139"):
    title = el.select('._1h3cgic > a')
    print( title[0].text)

URL = 'https://2gis.kg/bishkek/search/%D1%87%D0%B0%D1%81%D1%82%D0%BD%D1%8B%D0%B5%20%D0%BA%D0%BB%D0%B8%D0%BD%D0%B8%D0%BA%D0%B8%20%D0%B2%20%D0%B1%D0%B8%D1%88%D0%BA%D0%B5%D0%BA%D0%B5/page/2'

items = html.find_all('a', class_='_hc69qa')
print(items)