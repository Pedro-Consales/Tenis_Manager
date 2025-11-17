from socios_lib import (
    obter_socio,
    socio_ativo,
    vincular_convidado,
    eh_convidado,
    convidado_vinculado,
)

from socios_lib import OK, NAO_ENCONTRADO, INATIVO, INVALIDO, JA_EXISTE

print("\n============================")
print("   TESTES DO MÓDULO SÓCIOS  ")
print("============================\n")

# ============================================================
# Teste 1 – Sócio ativo existente
# ============================================================
print("TESTE 1 – obter_socio(1001): Sócio ativo existente")
resp = obter_socio(1001)
print("Retorno:", resp, "\n")


# ============================================================
# Teste 2 – Matrícula inexistente
# ============================================================
print("TESTE 2 – obter_socio(9999): Matrícula inexistente")
resp = obter_socio(9999)
print("Retorno:", resp, "\n")


# ============================================================
# Teste 3 – Sócio inativo
# ============================================================
print("TESTE 3 – obter_socio(1003): Sócio inativo")
resp = obter_socio(1003)
print("Retorno:", resp, "\n")


# ============================================================
# Testes de socio_ativo()
# ============================================================
print("TESTE 4 – socio_ativo(1001): ativo")
print("Retorno:", socio_ativo(1001), "\n")

print("TESTE 5 – socio_ativo(1003): inativo")
print("Retorno:", socio_ativo(1003), "\n")

print("TESTE 6 – socio_ativo(9999): inexistente")
print("Retorno:", socio_ativo(9999), "\n")


# ============================================================
# Testes de eh_convidado()
# ============================================================
print("TESTE 7 – eh_convidado(2001): é convidado")
print("Retorno:", eh_convidado(2001), "\n")

print("TESTE 8 – eh_convidado(1001): matrícula é sócio ativo (inválido)")
print("Retorno:", eh_convidado(1001), "\n")

print("TESTE 9 – eh_convidado(9999): inexistente")
print("Retorno:", eh_convidado(9999), "\n")


# ============================================================
# Testes de vincular_convidado()
# ============================================================
print("TESTE 10 – vincular_convidado(1001, 2001): já vinculado")
print("Retorno:", vincular_convidado(1001, 2001), "\n")

print("TESTE 11 – vincular_convidado(1003, 2001): sócio inativo")
print("Retorno:", vincular_convidado(1003, 2001), "\n")

print("TESTE 12 – vincular_convidado(1001, 1001): tentar vincular sócio ativo")
print("Retorno:", vincular_convidado(1001, 1001), "\n")

print("TESTE 13 – vincular_convidado(1001, 9999): convidado inexistente")
print("Retorno:", vincular_convidado(1001, 9999), "\n")


# ============================================================
# Testes de convidado_vinculado()
# ============================================================
print("TESTE 14 – convidado_vinculado(1001, 2001): convidado vinculado")
print("Retorno:", convidado_vinculado(1001, 2001), "\n")

print("TESTE 15 – convidado_vinculado(1001, 1001): sócio não pode ser convidado")
print("Retorno:", convidado_vinculado(1001, 1001), "\n")

print("TESTE 16 – convidado_vinculado(9999, 2001): sócio inexistente")
print("Retorno:", convidado_vinculado(9999, 2001), "\n")

print("TESTE 17 – convidado_vinculado(1001, 9999): convidado inexistente")
print("Retorno:", convidado_vinculado(1001, 9999), "\n")


print("\n============================")
print("       FIM DOS TESTES       ")
print("============================\n")
