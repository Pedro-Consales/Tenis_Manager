from django.contrib import admin
from django.urls import path
# from django.urls import include
from .views import show_menubase, show_quadras

urlpatterns = [
    path("", show_menubase, name='menu_base'),
    path("quadras/", show_quadras, name='quadras'),
]