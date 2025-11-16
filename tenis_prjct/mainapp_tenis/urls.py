from django.contrib import admin
from django.urls import path
from .Quadras.views_quadras import show_quadras, set_disponibilidade_false, set_disponibilidade_true, make_reserva
from .views import show_menubase

urlpatterns = [
    path("", show_menubase, name="menu_base"),
    path("quadras/", show_quadras, name="quadras"),

    path("set_disp_false/<int:quadra_id>/", set_disponibilidade_false, name="set-disp-false"),
    path("set_disp_true/<int:quadra_id>/", set_disponibilidade_true, name="set-disp-true"),

    # múltiplos parâmetros no path
    path("make_reserva/<int:quadra_id>/", make_reserva, name="make-reserva"),
]