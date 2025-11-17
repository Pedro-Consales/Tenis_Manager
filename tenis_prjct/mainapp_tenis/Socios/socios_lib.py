import json
from pathlib import Path

# Caminho para o arquivo JSON de sócios
DATA_PATH = Path(__file__).resolve().parent.parent / "socios_data.json"
print(DATA_PATH)
# Códigos de retorno padronizados
OK = 0
ERRO = 1
NAO_ENCONTRADO = 2
INATIVO = 3
INVALIDO = 4
JA_EXISTE = 5
LIMITE = 6
VAZIO = 7
SEM_PERMISSAO = 8
EM_ESPERA = 9


def load_socios():
    """
    Carrega a lista de sócios a partir do arquivo JSON.

    Retorna:
        list[dict]: lista de sócios; caso o arquivo não exista, retorna lista vazia.
    """
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            # Se o conteúdo não for lista, consideramos que não há sócios válidos
            return []
    except FileNotFoundError:
        # Arquivo ainda não criado: não é erro, apenas não há sócios cadastrados
        return []
    except Exception as exc:
        print(f"[SOCIOS] Erro ao carregar arquivo de sócios: {exc}")
        # Em caso de erro inesperado, ainda retornamos lista vazia para não quebrar o fluxo
        return []


def salvar_socios(socios_list):
    """
    Salva a lista de sócios no arquivo JSON.

    Args:
        socios_list (list[dict]): lista completa de sócios.

    Retorna:
        int: código de retorno (OK ou ERRO).
    """
    try:
        with open(DATA_PATH, "w", encoding="utf-8") as file:
            json.dump(socios_list, file, indent=4, ensure_ascii=False)
        return OK
    except Exception as exc:
        print(f"[SOCIOS] Erro ao salvar arquivo de sócios: {exc}")
        return ERRO


def normalizar_status(status):
    """
    Normaliza o campo de status para comparação.

    Considera 'ativo' e 'Ativo' equivalentes.
    """
    if not isinstance(status, str):
        return ""
    
    return status.strip().lower()


def socio_esta_ativo(socio_dict):
    """
    Retorna True se o sócio estiver com status ativo.
    """
    return normalizar_status(socio_dict.get("status", "")) == "ativo"


def get_socio_by_matricula(matricula, todos_socios):
    """
    Busca um sócio específico na lista em memória.

    Retorna:
        dict | None: dicionário do sócio ou None se não encontrado.
    """
    for socio in todos_socios:
        if socio.get("matricula") == matricula:
            return socio
    return None


def matricula_e_socio_ativo(matricula, todos_socios):
    """
    Verifica se uma matrícula pertence a um sócio ativo.

    Retorna:
        bool: True se for sócio ativo, False caso contrário.
    """
    socio = get_socio_by_matricula(matricula, todos_socios)
    return socio is not None and socio_esta_ativo(socio)


def obter_socio(matricula):
    """
    Retorna os dados completos do sócio correspondente à matrícula informada.

    Formato de retorno:
        {
            "codRetorno": <int>,
            "TpSocio": <dict | None>
        }

    Regras:
        - Caso 1 – Sócio ativo existente (ex: 1001):
            codRetorno = OK (0), TpSocio = dados do sócio (status "Ativo"/"ativo").
        - Caso 2 – Matrícula inexistente (ex: 9999):
            codRetorno = NAO_ENCONTRADO (2), TpSocio = None.
        - Caso 3 – Sócio inativo (ex: 1003):
            codRetorno = INATIVO (3), TpSocio = dados do sócio (opcional).
    """
    # Validação de tipo
    if not isinstance(matricula, int):
        return {"codRetorno": INVALIDO, "TpSocio": None}

    socios = load_socios()
    socio = get_socio_by_matricula(matricula, socios)

    if socio is None:
        return {"codRetorno": NAO_ENCONTRADO, "TpSocio": None}

    if socio_esta_ativo(socio):
        return {"codRetorno": OK, "TpSocio": socio}

    # Sócio encontrado, mas inativo
    return {"codRetorno": INATIVO, "TpSocio": socio}


def socio_ativo(matricula):
    """
    Confere se o sócio está com status 'ativo' no sistema.

    Retorna:
        int: código de retorno.
            - OK (0) se sócio ativo.
            - NAO_ENCONTRADO (2) se matrícula não existir.
            - INATIVO (3) se sócio existir mas estiver inativo.
            - INVALIDO (4) se matrícula for inválida.
    """
    if not isinstance(matricula, int):
        return INVALIDO

    socios = load_socios()
    socio = get_socio_by_matricula(matricula, socios)

    if socio is None:
        return NAO_ENCONTRADO

    if socio_esta_ativo(socio):
        return OK

    return INATIVO


def vincular_convidado(matricula_socio, matricula_convidado):
    """
    Associa um convidado a um sócio existente, garantindo que o convidado só
    possa participar de reservas vinculadas a esse sócio.

    Regras:
        - Só é permitido vincular convidados a sócios ATIVOS.
        - Uma matrícula que pertence a um sócio ativo não pode ser usada como convidado.
        - Um mesmo convidado não pode ser vinculado duas vezes ao mesmo sócio.
        - Opcionalmente, impede que o mesmo convidado seja vinculado
          a sócios diferentes (um convidado = um sócio).

    Retorna:
        int: código de retorno:
            - OK (0) em caso de sucesso.
            - INVALIDO (4) se alguma matrícula for inválida ou se a matrícula
              do convidado corresponder a um sócio ativo.
            - NAO_ENCONTRADO (2) se a matrícula do sócio não existir.
            - INATIVO (3) se o sócio estiver inativo.
            - JA_EXISTE (5) se o convidado já estiver vinculado ao sócio (ou já vinculado
              a qualquer sócio, dependendo da regra de negócio adotada).
            - ERRO (1) se houver falha ao salvar.
    """
    if not isinstance(matricula_socio, int) or not isinstance(matricula_convidado, int):
        return INVALIDO

    socios = load_socios()

    # Localiza o sócio responsável
    socio = get_socio_by_matricula(matricula_socio, socios)
    if socio is None:
        return NAO_ENCONTRADO

    # Sócio deve estar ativo
    if not socio_esta_ativo(socio):
        return INATIVO

    # Verifica se a matrícula do convidado corresponde a um sócio ativo
    if matricula_e_socio_ativo(matricula_convidado, socios):
        # Matrícula de sócio ativo não pode ser tratada como convidado
        return INVALIDO

    # Garante que o campo 'convidados' existe e é uma lista
    convidados = socio.get("convidados")
    if not isinstance(convidados, list):
        convidados = []
        socio["convidados"] = convidados

    # Regra: convidado já vinculado ao próprio sócio
    if matricula_convidado in convidados:
        return JA_EXISTE

    # Regra opcional: impedir um convidado de ser vinculado a mais de um sócio
    for outro_socio in socios:
        if outro_socio is socio:
            continue
        outros_convidados = outro_socio.get("convidados", [])
        if isinstance(outros_convidados, list) and matricula_convidado in outros_convidados:
            # Já vinculado a outro sócio
            return JA_EXISTE

    # Vincula convidado
    convidados.append(matricula_convidado)

    # Salva a lista de sócios atualizada
    result = salvar_socios(socios)
    if result != OK:
        return ERRO

    return OK


def eh_convidado(matricula):
    """
    Verifica se uma matrícula pertence a algum convidado vinculado a um sócio.

    Casos especificados:
        - Caso 1 – Matrícula corresponde a convidado (ex: 2001)
            Esperado: retorno True, código OK (0).
        - Caso 2 – Matrícula corresponde a sócio ativo (ex: 1001)
            Esperado: retorno False, código INVALIDO (4).
        - Caso 3 – Matrícula inexistente (ex: 9999)
            Esperado: retorno False, código NAO_ENCONTRADO (2).

    Retorna:
        tuple[bool, int]: (eh_convidado, codRetorno)
    """
    if not isinstance(matricula, int):
        return False, INVALIDO

    socios = load_socios()

    # Verifica se matrícula é de sócio ativo
    if matricula_e_socio_ativo(matricula, socios):
        return False, INVALIDO

    # Verifica se matrícula aparece na lista de convidados de algum sócio
    encontrado_como_convidado = False
    for socio in socios:
        convidados = socio.get("convidados", [])
        if isinstance(convidados, list) and matricula in convidados:
            encontrado_como_convidado = True
            break

    if encontrado_como_convidado:
        return True, OK

    # Não é sócio ativo nem consta em nenhuma lista de convidados
    # Agora verificamos se a matrícula existe como sócio inativo
    socio_inativo = get_socio_by_matricula(matricula, socios)
    if socio_inativo is not None:
        # Existe como sócio, mas não ativo → não deve ser tratado como convidado
        return False, INVALIDO

    # Matrícula completamente desconhecida
    return False, NAO_ENCONTRADO


def convidado_vinculado(matricula_socio, matricula_convidado):
    """
    Verifica se uma matrícula de convidado está vinculada a um determinado sócio.

    Essa função é útil para o módulo de reservas garantir que um convidado
    só participe de reservas se estiver vinculado ao sócio responsável.

    Regras de retorno:
        - OK (0) se o convidado estiver vinculado ao sócio informado.
        - NAO_ENCONTRADO (2) se o sócio não existir OU se o convidado não
          estiver vinculado ao sócio.
        - INVALIDO (4) se algum parâmetro for inválido ou se a matrícula do
          convidado corresponder a um sócio ativo (não deve ser tratado como convidado).
        - INATIVO (3) se o sócio estiver inativo.
    """
    if not isinstance(matricula_socio, int) or not isinstance(matricula_convidado, int):
        return INVALIDO

    socios = load_socios()
    socio = get_socio_by_matricula(matricula_socio, socios)

    if socio is None:
        return NAO_ENCONTRADO

    if not socio_esta_ativo(socio):
        return INATIVO

    # Um sócio ativo não pode ser considerado convidado
    if matricula_e_socio_ativo(matricula_convidado, socios):
        return INVALIDO

    convidados = socio.get("convidados", [])
    if not isinstance(convidados, list):
        convidados = []
        socio["convidados"] = convidados

    if matricula_convidado in convidados:
        return OK

    return NAO_ENCONTRADO
