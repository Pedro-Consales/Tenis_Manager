from quadras_lib import load_quadras


quadras = load_quadras()

for quadra in quadras:
    q_h = quadra.get('Horarios')
    for horarios in q_h:
        hr_i = horarios.get('Inicio')
        hr_f = horarios.get('Fim')
        reservas = horarios.get('Reservas', {})
        lista_socio = reservas.get('lista_socio_ids',[])
        print(f"Início: {hr_i} - Fim {hr_f}\n")
        print(f"Reservas: {reservas}\n")
        for soc_id in lista_socio:
            print(f"Lista: {soc_id}\n\n")


