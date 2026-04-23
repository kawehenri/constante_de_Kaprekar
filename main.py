"""Aplicacao principal para a atividade da Constante de Kaprekar."""

from src.crud_execucoes import (
    atualizar_observacao,
    criar_registro,
    excluir_registro,
    listar_registros,
)
from src.kaprekar import executar_rotina_kaprekar


def ler_inteiro():
    entrada = input("Informe um numero inteiro: ")
    try:
        numero = int(entrada)
    except ValueError:
        return None
    return numero


def escolher_modo():
    print("Selecione o modo de execucao:")
    print("1 - Rotina de 4 digitos (Constante 6174)")
    print("2 - Rotina de 3 digitos (Constante 495)")

    opcao = input("Opcao: ").strip()
    if opcao == "2":
        return 3
    return 4


def menu_crud():
    print("\n=== Menu principal ===")
    print("1 - Nova execucao da rotina (Create)")
    print("2 - Listar execucoes salvas (Read)")
    print("3 - Atualizar observacao de um registro (Update)")
    print("4 - Excluir registro (Delete)")
    print("0 - Sair")
    return input("Opcao: ").strip()


def executar_nova_rotina():
    digitos = escolher_modo()
    numero = ler_inteiro()

    if numero is None:
        print("Erro: o valor informado nao e um numero inteiro.")
        return

    print(f"\nNumero informado: {numero}")
    sucesso, mensagem, iteracoes = executar_rotina_kaprekar(numero, digitos)
    print()
    print(mensagem)

    registro = criar_registro(numero, digitos, sucesso, iteracoes, mensagem)
    print(f"\nRegistro salvo com ID {registro['id']}.")


def mostrar_registros():
    registros = listar_registros()
    if not registros:
        print("Nenhum registro salvo.")
        return

    print("\n=== Registros salvos ===")
    for item in registros:
        status = "Sucesso" if item["sucesso"] else "Erro"
        print(
            f"ID {item['id']} | num={item['numero']} | modo={item['digitos']}d | "
            f"{status} | iter={item['iteracoes']} | criado={item['criado_em']}"
        )
        if item["observacao"]:
            print(f"  Observacao: {item['observacao']}")


def atualizar_registro():
    registro_id = ler_inteiro()
    if registro_id is None:
        print("Erro: informe um ID inteiro.")
        return
    observacao = input("Nova observacao: ").strip()
    ok = atualizar_observacao(registro_id, observacao)
    if ok:
        print("Registro atualizado com sucesso.")
    else:
        print("Registro nao encontrado.")


def remover_registro():
    registro_id = ler_inteiro()
    if registro_id is None:
        print("Erro: informe um ID inteiro.")
        return
    ok = excluir_registro(registro_id)
    if ok:
        print("Registro excluido com sucesso.")
    else:
        print("Registro nao encontrado.")


def main():
    print("=== Rotina de Kaprekar ===")
    while True:
        opcao = menu_crud()
        if opcao == "1":
            executar_nova_rotina()
        elif opcao == "2":
            mostrar_registros()
        elif opcao == "3":
            print("Informe o ID do registro para atualizar:")
            atualizar_registro()
        elif opcao == "4":
            print("Informe o ID do registro para excluir:")
            remover_registro()
        elif opcao == "0":
            print("Encerrando aplicacao.")
            break
        else:
            print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    main()
