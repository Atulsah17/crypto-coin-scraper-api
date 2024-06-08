from celery import shared_task
from .coinmarketcap import CoinMarketCap

@shared_task
def get_coin_data_task(coin_acronyms):
    cmc = CoinMarketCap()
    return cmc.get_coin_data(coin_acronyms)
