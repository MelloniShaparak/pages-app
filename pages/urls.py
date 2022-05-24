from .views import HomePageView
from .views import AboutPageView
from .views import ContactPageView
from .views import PricePageView
from django.urls import path

urlpatterns = [
    path('price/', PricePageView.as_view(), name='price'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('home/', HomePageView.as_view(), name='home'), #new
    path('', HomePageView.as_view(), name='home'), #new

]
