from django.contrib import admin
from django.urls import path
from cities import views
from cities.views import RestaurantList

url_rlist = [
    path('', views.index, name='r_list'),
    path('list', RestaurantList.as_view(), name='list'),
    path('add', views.add_r, name='r_list'),
    path('rest/<int:id>/delete/', views.delete_r, name='delete_r'),
    path('rest/<int:id>/update/', views.update_r, name='update_r'),
    path('search', views.search_r, name='search_r'),
]
