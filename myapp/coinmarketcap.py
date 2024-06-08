import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class CoinMarketCap:
    def __init__(self):
        self.base_url = "https://coinmarketcap.com"

    def fetch_coin_data(self, coin_acronyms):
        data = {}
        for acronym in coin_acronyms:
            data[acronym] = self.scrape_coin_data(acronym)
        return data

    def scrape_coin_data(self, acronym):
        url = f"{self.base_url}/currencies/{acronym}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Scraping logic to extract the necessary data
        price_tag = soup.find('div', class_='priceValue___11gHJ')
        price = price_tag.text if price_tag else 'N/A'
        
        return {'price': price}

    def get_coin_data(self, coin_acronyms):
        return self.fetch_coin_data(coin_acronyms)
