"""CRUD simples de execucoes da rotina de Kaprekar."""

from datetime import datetime
import json
import os


ARQUIVO_REGISTROS = "data/registros_execucoes.json"


def _garantir_arquivo():
    pasta = os.path.dirname(ARQUIVO_REGISTROS)
    if pasta and not os.path.exists(pasta):
        os.makedirs(pasta, exist_ok=True)

    if not os.path.exists(ARQUIVO_REGISTROS):
        with open(ARQUIVO_REGISTROS, "w", encoding="utf-8") as arquivo:
            json.dump([], arquivo, ensure_ascii=True, indent=2)


def listar_registros():
    _garantir_arquivo()
    with open(ARQUIVO_REGISTROS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def _salvar_registros(registros):
    _garantir_arquivo()
    with open(ARQUIVO_REGISTROS, "w", encoding="utf-8") as arquivo:
        json.dump(registros, arquivo, ensure_ascii=True, indent=2)


def criar_registro(numero, digitos, sucesso, iteracoes, mensagem):
    registros = listar_registros()
    novo_id = 1
    if registros:
        ultimo_id = registros[-1]["id"]
        novo_id = ultimo_id + 1

    resumo = mensagem.splitlines()[0] if mensagem else ""
    registro = {
        "id": novo_id,
        "numero": numero,
        "digitos": digitos,
        "sucesso": sucesso,
        "iteracoes": iteracoes,
        "resumo": resumo,
        "criado_em": datetime.now().isoformat(timespec="seconds"),
        "observacao": "",
    }
    registros.append(registro)
    _salvar_registros(registros)
    return registro


def atualizar_observacao(registro_id, observacao):
    registros = listar_registros()
    for item in registros:
        if item["id"] == registro_id:
            item["observacao"] = observacao
            _salvar_registros(registros)
            return True
    return False


def excluir_registro(registro_id):
    registros = listar_registros()
    nova_lista = []
    removido = False
    for item in registros:
        if item["id"] == registro_id:
            removido = True
        else:
            nova_lista.append(item)

    if removido:
        _salvar_registros(nova_lista)
    return removido
