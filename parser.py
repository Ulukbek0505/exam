
import requests
from bs4 import BeautifulSoup as BS

def get_response(url):
    response = requests.get(url)  # delete # head # post # put...
    if response.status_code == 200:
        return response.text
    else:
        return "не успешный запрос по url !"


def pizzas_list(html):
    soup = BS(html, "html.parser")
    content = soup.find('div', class_= "holiday-decoration menu-bg")
    title_price = content.find_all("div", class_= "bottom-block_1wBkV")
    for info in title_price:
        title = info.find("div", class_="title_3uNTc").text.strip()
        price = info.find("div", class_="price_1_Tty").text.strip()
        tit_price_dict = {title}, {price}
        return tit_price_dict

        print(())


my_html = get_response('https://3332222.ru/menu/picca/')
print(pizzas_list(my_html))