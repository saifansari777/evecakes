from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
		path('', views.index, name="index"),
		path('list/', views.CakeList.as_view(), name='cake-list'),
		path('list/<slug>/', views.CakeDetail.as_view(), name='cake-detail'),
		path('trash', views.banner, name='trash'),
]
