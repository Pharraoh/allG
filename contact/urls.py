from django.conf.urls import url
from . import views

app_name = "contact"

urlpatterns = [
    url('contact/', views.contact, name = 'contact'),
    url('faq/', views.faq, name = 'faq'),
]
