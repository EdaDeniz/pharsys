from django.conf.urls import url
import carts
from . import views
from .views import cart_view, update_cart, delete_cart

app_name = "cart"



urlpatterns = [

       url(r'^cart/$', cart_view, name="cart"),
       url(r'^cart/(?P<id>\d+)/$', update_cart, name="update_cart"),
       url(r'^cart/delete/$', delete_cart, name="delete_cart"),


    ]
