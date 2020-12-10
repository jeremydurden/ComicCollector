from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('comics/', views.comics_index, name='index'),
    path('comics/<int:comic_id>/', views.comics_detail, name='detail')
]