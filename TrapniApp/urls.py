from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="update_item"),
    path('event/', views.event, name="event"),
    path('', views.main, name="main"),
]