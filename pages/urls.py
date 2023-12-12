from django.conf.urls import url
from . import views

app_name = "pages"

urlpatterns = [
    url(r"^terms/$", views.terms, name = "terms"),
    url(r"^testimonials/$", views.testimonials, name = "testimonials"),
    url(r"^recover_password/$", views.recover_password, name = "recover_password"),
]
