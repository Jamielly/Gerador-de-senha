# Gerador de Senhas em Python 👾

Este é um simples gerador de senhas em Python que gera senhas aleatórias únicas misturando letras maiúsculas, minúsculas, números e símbolos. O código foi desenvolvido seguindo as boas práticas de segurança da informação. E como modo de facilitar preguiçosos como eu, ou pouco criativos em gerar suas suas senhas pessoais. 🤷‍♀️

## Como Funciona? 👇

O gerador de senhas utiliza a biblioteca `random` do Python para gerar caracteres aleatórios e a biblioteca `string` para obter os conjuntos de caracteres a serem usados na criação das senhas.

O programa consiste em duas funções principais:

1. `gerar_senha(tamanho)`: Esta função gera uma senha aleatória com o tamanho especificado. Ela usa a função `random.choice()` para selecionar caracteres aleatórios de um conjunto de caracteres que inclui letras maiúsculas, minúsculas, números e símbolos.

2. `gerar_senhas_unicas(numero_senhas)`: Esta função gera um número especificado de senhas únicas. Ela mantém uma lista de senhas geradas anteriormente para garantir que as senhas geradas sejam realmente únicas.

## Como Utilizar 🤔

1. Clone este repositório para o seu ambiente local.
2. Execute o arquivo `gerador_senhas.py` utilizando o Python.
3. O programa imprimirá até cinco senhas únicas no terminal.

## Personalização 🤩

Você pode personalizar o tamanho das senhas alterando o valor do parâmetro `tamanho` na função `gerar_senha(tamanho)`. Por padrão, as senhas têm 12 caracteres de comprimento.

Além disso, você pode ajustar o número máximo de senhas geradas modificando o valor do parâmetro `numero_senhas` na função `gerar_senhas_unicas(numero_senhas)`.

