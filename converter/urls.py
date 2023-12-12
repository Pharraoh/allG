from django.conf.urls import url
from . import views

app_name = "converter"

urlpatterns = [
    url('alerts/', views.alerts, name = 'alerts'),
    url('chart/', views.chart, name = 'chart'),
    url('converter/', views.converter, name = 'converter'),
    url('send_money/', views.send_money, name = 'send_money')
]
