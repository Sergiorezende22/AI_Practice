# Explicação do exercício

## Notebook
O notebook '8-puzzle.ipynb' contém toda a implementação do exercício com explicações no markdown.

## Implementação em arquivos
Os arquivos '.py' são as implementações dos exercícios de maneira serapada para obter os resultados da maneira que foram pedidas. Para utilizar, basta rodar o arquivo 8-puzzle.py com os argumentos corretos:

    - Método 
    - Estado da seguinte forma: 0,1,2,3,4,5,6,7,8
    - No caso do idfs o minimo, maximo e o passo que a iteração vai ocorrer.

Exemplos:

    - python3 8-puzzle.py bfs 0,8,7,6,5,4,3,2,1
    - python3 8-puzzle.py idfs 0,8,7,6,5,4,3,2,1 1000 15000 1000

Métodos implementados:

    - bfs
    - dfs
    - idfs
    - astar
    - greedy

## Resultados
Por fim, os resultados rodados na minha máquina com o exemplo dado no exercício(0,8,7,6,5,4,3,2,1 como estado inicial) está na pasta 'ans', no arquivo correspondente ao método.