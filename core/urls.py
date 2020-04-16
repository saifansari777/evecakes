from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
		path('', views.index, name="index"),
		path('list/', views.ItemList.as_view(), name='item-list'),
		path('list/<slug>/', views.ItemDetail.as_view(), name='item-detail'),
		path('trash', views.banner, name='trash'),
]
