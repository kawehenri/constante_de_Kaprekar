# Kaprekar Routine Analyzer

Projeto academico profissional para demonstrar a Rotina de Kaprekar:
- 4 digitos -> constante `6174` (obrigatorio no edital).
- 3 digitos -> constante `495` (extensao para mencao honrosa).

## Objetivo
Implementar um algoritmo iterativo com validacoes formais de entrada, exibindo passo a passo as subtracoes ate atingir a constante de Kaprekar.

## Requisitos atendidos
- Validacao de tipo (numero inteiro).
- Validacao de sinal (inteiro positivo).
- Validacao de faixa:
  - `0000` a `9999` para 4 digitos.
  - `000` a `999` para 3 digitos.
- Validacao de repeticao de digitos (bloqueia 3 ou mais iguais).
- Construcao de NDC e NDD.
- Subtracao `NDD - NDC`.
- Iteracao ate constante.
- Exibicao de cada iteracao.

## Restricoes tecnicas do edital
A manipulacao de digitos foi feita por operacoes aritmeticas:
- divisao inteira (`//`)
- resto da divisao (`%`)
- comparacoes e trocas

Sem bibliotecas externas para o algoritmo.

## Estrutura do repositorio
- `main.py`: interface simples para executar no terminal.
- `src/kaprekar.py`: implementacao da rotina e validacoes.
- `src/crud_execucoes.py`: CRUD simples para salvar e gerenciar execucoes.
- `notebooks/kaprekar_colab.ipynb`: versao pronta para Google Colab.
- `docs/roteiro_apresentacao.md`: roteiro oral.
- `docs/diagrama_fluxo.md`: fluxograma Mermaid.
- `docs/checklist_entrega.md`: checklist para AVA e GitHub.

## Menu CRUD no terminal
Ao executar `main.py`, voce pode:
- Criar uma nova execucao da rotina.
- Listar execucoes ja salvas.
- Atualizar a observacao de um registro salvo.
- Excluir um registro.

Os registros ficam em `data/registros_execucoes.json`.

## Como executar localmente
1. Abra um terminal na pasta do projeto.
2. Para versao terminal, execute:

```bash
python main.py
```

3. Para versao com janela (GUI), execute:

```bash
python app_gui.py
```

## Janela (GUI) profissional
- Interface com formulario de nova execucao.
- Tabela com historico de execucoes salvas.
- Atualizacao de observacao por ID.
- Exclusao de registro por ID.

Na versao terminal (`main.py`):
- Escolha o modo:
  - `1` para 4 digitos (6174)
  - `2` para 3 digitos (495)
- Informe um numero inteiro.

## Exemplo (4 digitos)
Entrada: `3524`

Saida esperada:
- Iteracao 1: `5432 - 2345 = 3087`
- Iteracao 2: `8730 - 0378 = 8352`
- Iteracao 3: `8532 - 2358 = 6174`

## Publicacao no GitHub
Sugestao de nome do repositorio:
- `kaprekar-routine-analyzer`

Sugestao de descricao:
- `Academic implementation of Kaprekar routine (6174 and 495) using arithmetic digit manipulation.`
