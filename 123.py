from bs4 import BeautifulSoup
import requests

def parse():
    URL = 'https://4frag.ru/specials/'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
    }

    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'item-product-inner product-special-big-block')
    devices = []

    for item in items:
        devices.append ({
            'price': item.find('span', class_='item-price').get_text(strip = True),
            'price_old': item.find('span', class_='item-price-old').get_text(strip = True),
            'title': item.find( 'a', class_ = 'item-link').get_text(strip = True),
            'link': item.find( 'a', class_ = 'item-link').get('href')

        })
    for device in devices:
        print (f'\n Товар: {device["title"]}\n Новая цена: {device["price"]} \n Старая цена {device["price_old"]} \n Ссылка: {device["link"]}')
parse()


