from django.shortcuts import render, redirect
from django.contrib import messages
from .quadras_lib import salvar_quadras,load_quadras, get_quadra_by_id

DEFAULT_QUADRA_NOME = "A quadra"

# Uma Sócio só pode reservar a quadra se ela estiver disponível e não estiver interditada.
# Através de um "modelo" participação: Que deve possuir um horário de início e fim da reserva.

#Chamo a função que retorna a lista de quadras com todas as quadras criadas (HardCoded) no arquivo quadras_lib.py

#Exibo o html da página de quadras

def show_quadras(request):

    lista_quadras = load_quadras()
    context = {
        'lista_quadras': lista_quadras
    }

    return render(request, "partials/quadras.html", context)



def set_disponibilidade_false(request, quadra_id):

    if request.method != "POST":
        return redirect('quadras')

    quadras = load_quadras()

    if isinstance(quadras, int):
        print("\nErro ao carregar quadras.\n")
        return redirect("quadras")

    quadra = get_quadra_by_id(quadra_id, quadras)
    if quadra == -1:
        print(f"\nQuadra {quadra_id} não encontrada.\n")
        return redirect("quadras")
    print("\nQuadra encontada pelo get_quadra_by_id\n")
    print(f"Quadra {quadra}")
   
    quadra["Disponivel"] = False


    salvar_quadras(quadras)
    return redirect("quadras")


def set_disponibilidade_true(request, quadra_id):
     
    if request.method != "POST":
        return redirect('quadras')

    quadras = load_quadras()

    if isinstance(quadras, int):
        print("\nErro ao carregar quadras.\n")
        return redirect("quadras")

    quadra = get_quadra_by_id(quadra_id, quadras)
    if quadra == -1:
        print(f"\nQuadra {quadra_id} não encontrada.\n")
        return redirect("quadras")
    print("\nQuadra encontada pelo get_quadra_by_id\n")
    print(f"Quadra {quadra}")
   
    quadra["Disponivel"] = True
    

    salvar_quadras(quadras)
    return redirect("quadras")
    


def get_quadra(request, quadra_id):
    
    if request.method != 'POST':
        return redirect('quadras')
    
    quadra = get_quadra_by_id(quadra_id)
     
    if quadra == -1: # Quadra não encontrada
        quadra_nome = quadra['Nome']
        if quadra_nome is None:
            quadra_nome = DEFAULT_QUADRA_NOME #Nome padrão caso o nome da quadra não esteja definido

        messages.error(request, f"{quadra_nome} não foi encontrada.")
        return redirect('quadras')
    
    if quadra == -2: # Quadra indisponível

        quadra_nome = quadra['Nome']
        if quadra_nome is None:
            quadra_nome = DEFAULT_QUADRA_NOME #Nome padrão caso o nome da quadra não esteja definido

        messages.error(request, f"{quadra_nome} indisponível.")
        return redirect('quadras')
    
    if quadra == -3: # Quadra interditada

        quadra_nome = quadra['Nome']
        if quadra_nome is None:
            quadra_nome = DEFAULT_QUADRA_NOME #Nome padrão caso o nome da quadra não esteja definido
            
        messages.error(request, f"{quadra_nome} interidtada por manutenção ou condições climáticas.")
        return redirect('quadras')        

    return redirect('quadras')