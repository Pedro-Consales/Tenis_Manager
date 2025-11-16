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
    

def make_reserva(request, quadra_id): #Pode ser que não dê para buscar daqui. Tenhamos que usar resquest.POST.get

    todas_quadras = load_quadras()
    if isinstance(todas_quadras, int):
        messages.error(request, "Erro ao carregar quadras.")
        return redirect("quadras")

    if request.method != 'POST':
        return redirect('quadras')
    
    try:
        horario = request.POST.get("horario_inicio")
    except (TypeError, ValueError):
        messages.error(request, "Horário inválido.")
        return redirect("quadras")
    
    matricula_socio = request.POST.get("matricula", "").strip()
    if not matricula_socio:
        messages.error(request, "Informe a matrícula do associado.")
        return redirect("quadras")
    print(f"\nMatricula do Socio {matricula_socio}\n")
    
    quadra = get_quadra_by_id(quadra_id, todas_quadras)
    if quadra == -1:
        messages.error(request, "Quadra não encontrada.")
        print("\nQuadra não encontrada. cod: -1\n")
        return redirect("quadras")


    horarios_all = quadra["Horarios"]
    print(f"\nTodos os horários {horarios_all}\n")

    for h in horarios_all:
        h_inicio = h["Inicio"]
        print(f"h_início: {h_inicio}\n")
        if h_inicio == horario:  # bingo
            horario_dict = h
            print(f"Horário_dict: {horario_dict}\n")
            
            print(f"Horário escolhido: {h_inicio}\n")

            break

    if horario_dict is None:
        messages.error(request, "Horário não encontrado na quadra.")
        print("\nHorário não encontrado na quadra. NONE\n")
        return redirect("quadras")

    reservas = horario_dict["Reservas"]
    print(f"\nReservas antes de adicionar: {reservas}\n")
    lista_socios_ids = reservas["lista_socio_ids"]
    print(f"\nLista de sócios antes de adicionar: {lista_socios_ids}\n")


    try:
        matricula_int = int(matricula_socio)
    except ValueError:
        messages.error(request, "System erros at matrícula")
        print("ERRO: Matricula deve ser int")
        return redirect("quadras")

    if matricula_int not in lista_socios_ids:
        lista_socios_ids.append(matricula_int)
    else:
        messages.error("Esse sócio já está vinculado nessa reserva")

    print(f"\nLista de sócios após adicionar: {lista_socios_ids}\n")
    
    salvar_quadras(todas_quadras)


    quadra["Count_reservas"] = sum(
        len(slot.get("Reservas", {}).get("lista_socio_ids", []))
        for slot in horarios_all
    )

    salvar_quadras(todas_quadras)
    messages.success(request, f"Reserva na {quadra["Nome"]} às {h_inicio} registrada.")
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