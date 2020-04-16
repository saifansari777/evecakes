from django.urls import path
from . import views

app_name = 'cart'

urlpatterns =[
			path('', views.cart, name='cart'),
			path('add-to-cart/<slug>/', views.add_to_cart, name="add-to-cart"),
			path('remove-from-cart/<slug>/', views.remove_from_cart, name="remove-from-cart"),
			path('order-summary/', views.OrderSummary.as_view(), name="order-summary"),
	 ]