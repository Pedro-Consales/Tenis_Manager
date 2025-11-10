from django.contrib import admin
from django.urls import path
# from django.urls import include
from .Quadras.views_quadras import show_quadras
from .views import show_menubase

urlpatterns = [
    path("", show_menubase, name='menu_base'),
    path("quadras/", show_quadras, name='quadras'),
]