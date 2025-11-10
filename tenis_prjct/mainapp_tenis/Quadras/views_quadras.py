from django.shortcuts import render
from .quadras_lib import all_quadras, get_quadra_by_id

# Uma Sócio só pode reservar a quadra se ela estiver disponível e não estiver interditada.
# Através de um "modelo" participação: Que deve possuir um horário de início e fim da reserva.


lista_quadras = all_quadras()
#Chamo a função que retorna a lista de quadras com todas as quadras criadas (HardCoded) no arquivo quadras_lib.py

#Exibo o html da página de quadras

def show_quadras(request, lista_quadras=lista_quadras):

    return render(request, "partials/quadras.html", {'lista_quadras': lista_quadras})


#Exibo o html da página de detalhes da quadra