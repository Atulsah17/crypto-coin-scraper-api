from django.urls import path
from .views import CoinDataView

urlpatterns = [
    path('api/coin-data/', CoinDataView.as_view(), name='coin-data')
]
