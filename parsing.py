import requests
from bs4 import BeautifulSoup

def pogoda_in_semey():
    url = "https://tengrinews.kz/weather/semey/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    weather_block = soup.find('div', class_="temp")
    weather_info = weather_block.get_text().strip()
    pagodka =  'Погода в Семее: ' + weather_info
    return pagodka
def pogoda_in_taraz():
    url = "https://tengrinews.kz/weather/taraz/day/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    weather_block = soup.find('div', class_="temp")
    weather_info = weather_block.get_text().strip()
    pagodka =  'Погода в Таразе: ' + weather_info
    return pagodka

def pogoda_in_atyrau():
    url = "https://tengrinews.kz/weather/atyrau/day/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    weather_block = soup.find('div', class_="temp")
    weather_info = weather_block.get_text().strip()
    pagodka =  'Погода в Атырау: ' + weather_info
    return pagodka
def pogoda_in_almaty():
    url = "https://tengrinews.kz/weather/almaty/day/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    weather_block = soup.find('div', class_="temp")
    weather_info = weather_block.get_text().strip()
    pagodka =  'Погода в Алматы: ' + weather_info
    return pagodka
def pogoda_in_astana():
    url = "https://tengrinews.kz/weather/astana/day/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    weather_block = soup.find('div', class_="temp")
    weather_info = weather_block.get_text().strip()
    pagodka =  'Погода в Астана: ' + weather_info
    return pagodka
def pogoda_in_aktau():
    url = "https://tengrinews.kz/weather/aktau/day/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    weather_block = soup.find('div', class_="temp")
    weather_info = weather_block.get_text().strip()
    pagodka =  'Погода в Актау: ' + weather_info
    return pagodka
def news():
    url = "https://tengrinews.kz/tag/%D1%81%D0%B5%D0%BC%D0%B5%D0%B9/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    weather_block = soup.find('span', class_="tn-hidden")
    weather_info = weather_block.get_text().strip()
    pagodka = 'Последние новости в Семее:\n' + weather_info
    return pagodka

def kurs_dollar():
    url = "https://banki24.kz/kurs/nbrk/dollar"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    weather_block = soup.find('span', class_="display-1 text-hamburger font-weight-bold text-nowrap")
    weather_info = weather_block.get_text().strip()
    pagodka = weather_info + "  за 1 доллар"
    return pagodka

def kurs_euro():
    url = "https://banki24.kz/kurs/nbrk/evro"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    weather_block = soup.find('span', class_="display-1 text-hamburger font-weight-bold text-nowrap")
    weather_info = weather_block.get_text().strip()
    pagodka = weather_info + "  за 1 евро"
    return pagodka

def kurs_rub():
    url = "https://banki24.kz/kurs/nbrk/rossijskij-rubl"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    weather_block = soup.find('span', class_="display-1 text-hamburger font-weight-bold text-nowrap")
    weather_info = weather_block.get_text().strip()
    pagodka = weather_info + "  за 1 российский рубль"
    return pagodka

def kurs_chy():
    url = "https://banki24.kz/kurs/nbrk/kitajskij-yuan"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    weather_block = soup.find('span', class_="display-1 text-hamburger font-weight-bold text-nowrap")
    weather_info = weather_block.get_text().strip()
    pagodka = weather_info + "  за 1 китайский юань"
    return pagodka

def last_news():
    url = "https://informburo.kz/"
    req = requests.get(url)
    Soup = BeautifulSoup(req.content, 'html.parser')
    News = Soup.find_all(class_="uk-nav uk-nav-default")

    def last_newss():
        for item in News:
            ling = item.find_all('a', href=True)
            for tag in ling:
                tekst = tag.text.strip()
                cod = tag['href']
                print('Время:', f"{tekst}")
                print(f"Ссылка:{cod}")
                print()
    last_newss()