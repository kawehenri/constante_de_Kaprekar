# Roteiro de apresentacao oral

## 1) Contexto matematico
- A Rotina de Kaprekar reorganiza os digitos de um numero para formar NDD e NDC.
- Em seguida calcula `NDD - NDC`.
- Repetindo o processo, para numeros elegiveis de 4 digitos, atinge-se `6174`.
- Na extensao de 3 digitos, atinge-se `495`.

## 2) Estrutura do algoritmo
1. Ler entrada do usuario.
2. Validar tipo e sinal.
3. Validar faixa numerica.
4. Validar repeticao de digitos.
5. Extrair digitos com operacoes aritmeticas.
6. Ordenar digitos por comparacoes.
7. Construir NDC e NDD.
8. Subtrair e repetir ate a constante.

## 3) Ponto tecnico importante
- Nao foi usado array ou string para manipular digitos.
- A extracao usa apenas `//` e `%`.
- A ordenacao foi feita com trocas manuais.

## 4) Demonstracao sugerida
- Teste valido 4 digitos: `3524`.
- Teste valido 3 digitos: `352`.
- Teste invalido por repeticao: `7777`.
- Teste invalido por faixa: `10000`.
- Teste invalido por tipo: `abc`.

## 5) Fechamento
- Mostrar no GitHub a organizacao em pastas.
- Reforcar aderencia ao edital.
- Explicar rapidamente o fluxograma.
