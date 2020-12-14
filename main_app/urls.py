from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('comics/', views.comics_index, name='index'),
    path('comics/<int:comic_id>/', views.comics_detail, name='detail'),
    path('comics/create/', views.ComicCreate.as_view(), name='comics_create'),
    path('comics/<int:pk>/update/', views.ComicUpdate.as_view(), name='comics_update'),
    path('comics/<int:pk>/delete/', views.ComicDelete.as_view(), name='comics_delete'),
    path('comics/<int:comic_id>/add_cover/', views.add_cover, name='add_cover'),
    path('heroes/', views.HeroList.as_view(), name='heroes_index'),
    path('heroes/<int:pk>/', views.HeroDetail.as_view(), name='heroes_detail'),
    path('heroes/create/', views.HeroCreate.as_view(), name='heroes_create'),
    path('heroes/<int:pk>/update/', views.HeroUpdate.as_view(), name='heroes_update'),
    path('heroes/<int:pk>/delete/', views.HeroDelete.as_view(), name='heroes_delete'),
    path('heroes/<int:comic_id>/assoc_hero/<int:hero_id>/', views.assoc_hero, name='assoc_hero')

]