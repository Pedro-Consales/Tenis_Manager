def all_quadras():

    quadra1 = {
    'Nome': 'Quadra 1',
    'Id': 10, 
    'Tipo': 'Saibro',
    'Capacidade': 4, 
    'Disponivel': True,
    'Interditado': False,
    }

    quadra2 = {
        'Nome': 'Quadra 2',
        'Id': 11, 
        'Tipo': 'Grama',
        'Capacidade': 2, 
        'Disponivel': True,
        'Interditado': False,
    }

    quadra3 = {
        'Nome': 'Quadra 3',
        'Id': 12, 
        'Tipo': 'Dura',
        'Capacidade': 4, 
        'Disponivel': True,
        'Interditado': False,
    }

    quadra4 = {
        'Nome': 'Quadra 4',
        'Id': 13, 
        'Tipo': 'Carpet',
        'Capacidade': 2, 
        'Disponivel': True,
        'Interditado': True,
    }

    quadra5 = {
        'Nome': 'Quadra 5',
        'Id': 14, 
        'Tipo': 'Saibro',
        'Capacidade': 4, 
        'Disponivel': True,
        'Interditado': False,
    }

    lista_quadras = [quadra1, quadra2, quadra3, quadra4, quadra5]
    return lista_quadras



def get_quadra_by_id(quadra_id):
    todas_quadras = all_quadras()
    for quadra in todas_quadras:
        if quadra['Id'] == quadra_id:
            return quadra
    return -1  # Retorna -1 se a quadra não for encontrada