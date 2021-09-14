from bs4 import BeautifulSoup
import requests

URL = 'https://coinmarketcap.com/ru/currencies/smooth-love-potion/'

def get_html(url, params=None):
    r = requests.get(url, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    slp_price = soup.find('div', class_='priceValue').getText().replace('₽', '')
    return slp_price

def slp_take_price():
    html = get_html(URL)
    if html.status_code == 200:
        return get_content(html.text)
    else:
        print('Нет подключения к CoinMarket')