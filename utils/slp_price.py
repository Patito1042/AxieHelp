from bs4 import BeautifulSoup
import requests


def get_html(url, params=None):
    r = requests.get(url, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    slp_price = soup.find('div', class_='priceValue').getText()
    slp_price = slp_price.replace(slp_price[0], '')
    return slp_price

def slp_take_price(currencies):
    currencies_result = ''
    if currencies == 'USD':
        currencies_result = 'en'
    elif currencies == 'RUB':
        currencies_result = 'ru'
    URL = f'https://coinmarketcap.com/{currencies_result}/currencies/smooth-love-potion/'
    html = get_html(URL)
    if html.status_code == 200:
        return get_content(html.text)
    else:
        print('Нет подключения к CoinMarket')