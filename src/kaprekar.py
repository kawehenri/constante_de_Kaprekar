"""Rotina de Kaprekar com operacoes aritmeticas.

Este modulo evita uso de arrays e processamento de texto para manipular digitos.
"""


def extrair_4_digitos(numero):
    d1 = numero // 1000
    resto = numero % 1000
    d2 = resto // 100
    resto = resto % 100
    d3 = resto // 10
    d4 = resto % 10
    return d1, d2, d3, d4


def extrair_3_digitos(numero):
    d1 = numero // 100
    resto = numero % 100
    d2 = resto // 10
    d3 = resto % 10
    return d1, d2, d3


def ordenar_4_crescente(a, b, c, d):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if c > d:
        c, d = d, c
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c, d


def ordenar_3_crescente(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c


def max_repeticoes_4(a, b, c, d):
    cont_a = 1 + (1 if a == b else 0) + (1 if a == c else 0) + (1 if a == d else 0)
    cont_b = 1 + (1 if b == a else 0) + (1 if b == c else 0) + (1 if b == d else 0)
    cont_c = 1 + (1 if c == a else 0) + (1 if c == b else 0) + (1 if c == d else 0)
    cont_d = 1 + (1 if d == a else 0) + (1 if d == b else 0) + (1 if d == c else 0)

    maior = cont_a
    if cont_b > maior:
        maior = cont_b
    if cont_c > maior:
        maior = cont_c
    if cont_d > maior:
        maior = cont_d
    return maior


def max_repeticoes_3(a, b, c):
    cont_a = 1 + (1 if a == b else 0) + (1 if a == c else 0)
    cont_b = 1 + (1 if b == a else 0) + (1 if b == c else 0)
    cont_c = 1 + (1 if c == a else 0) + (1 if c == b else 0)

    maior = cont_a
    if cont_b > maior:
        maior = cont_b
    if cont_c > maior:
        maior = cont_c
    return maior


def validar_entrada(numero, digitos):
    if numero <= 0:
        return False, "Erro: o numero precisa ser inteiro e positivo."

    if digitos == 4:
        if numero < 0 or numero > 9999:
            return False, "Erro: para 4 digitos, informe um valor entre 0000 e 9999."
        a, b, c, d = extrair_4_digitos(numero)
        if max_repeticoes_4(a, b, c, d) >= 3:
            return False, "Erro: o numero possui muitos digitos repetidos (3 ou mais iguais)."
    elif digitos == 3:
        if numero < 0 or numero > 999:
            return False, "Erro: para 3 digitos, informe um valor entre 000 e 999."
        a, b, c = extrair_3_digitos(numero)
        if max_repeticoes_3(a, b, c) >= 3:
            return False, "Erro: o numero possui muitos digitos repetidos (3 ou mais iguais)."
    else:
        return False, "Erro interno: quantidade de digitos invalida."

    return True, ""


def passo_kaprekar(numero, digitos):
    if digitos == 4:
        a, b, c, d = extrair_4_digitos(numero)
        a, b, c, d = ordenar_4_crescente(a, b, c, d)
        ndc = a * 1000 + b * 100 + c * 10 + d
        ndd = d * 1000 + c * 100 + b * 10 + a
        return ndd, ndc, ndd - ndc

    a, b, c = extrair_3_digitos(numero)
    a, b, c = ordenar_3_crescente(a, b, c)
    ndc = a * 100 + b * 10 + c
    ndd = c * 100 + b * 10 + a
    return ndd, ndc, ndd - ndc


def executar_rotina_kaprekar(numero, digitos):
    constante = 6174 if digitos == 4 else 495
    largura = 4 if digitos == 4 else 3

    valido, mensagem = validar_entrada(numero, digitos)
    if not valido:
        return False, mensagem, 0

    iteracoes = 0
    atual = numero
    historico = ""

    while atual != constante:
        valido, mensagem = validar_entrada(atual, digitos)
        if not valido:
            return False, mensagem, iteracoes

        ndd, ndc, resultado = passo_kaprekar(atual, digitos)
        iteracoes += 1
        historico += (
            f"Iteracao {iteracoes}: "
            f"{ndd:0{largura}d} - {ndc:0{largura}d} = {resultado:0{largura}d}\n"
        )
        atual = resultado

    historico += (
        f"\nConstante de Kaprekar ({constante}) atingida em {iteracoes} iteracoes."
    )
    return True, historico, iteracoes
