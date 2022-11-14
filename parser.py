
import requests
from bs4 import BeautifulSoup as BS


def get_response(url):
    response = requests.get(url)  # delete # head # post # put...
    if response.status_code == 200:
        return response.text
    else:
        return "не успешный запрос по url !"


def pizza_mafia(html):
    data ={}
    soup = BS(html, "html.parser")
    content = soup.find('div', class_="holiday-decoration menu-bg")
    title_price = content.find_all("a", class_="card_1C7cu")
    for info in title_price:
        title = info.find("div", class_="title_3uNTc").text.strip()
        price = info.find("div", class_="price_1_Tty").text.strip()
        if title == 'Петровская 25 см (толстое с сыром)':
            break
        data.update({title: price})
    return data

def pizza30cm(html):
    global menu2
    data = {}
    soup = BS(html, "html.parser")
    content = soup.find('div', class_="my-catalog uk-section-default uk-section")
    in_title_price = content.find_all("div", {"class": "uk-card uk-card-default uk-card-small"})
    for info in in_title_price:
        title = info.find("h2", class_="uk-h4 uk-margin-small-bottom woocommerce-loop-product__title").text.strip()
        price = info.find("span", class_="woocommerce-Price-amount amount").text.strip()
        if title == 'Ранч':
            break
        data.update({title:price})

    return data

my_html = get_response('https://3332222.ru/menu/picca/')
print(pizza_mafia(my_html))
my_html1 = get_response('https://pizza30cm.ru/?utm_source=yandex&utm_campaign=%5Bpicca-spb%5D--MK_Con&utm_medium=cpc&utm_term=---autotargeting&utm_content=creative1&_openstat=ZGlyZWN0LnlhbmRleC5ydTs3NDE1ODY3MjsxMjExMDIzOTc2MDt5YW5kZXgucnU6cHJlbWl1bQ&yclid=842516730018529279')
print(pizza30cm(my_html1))