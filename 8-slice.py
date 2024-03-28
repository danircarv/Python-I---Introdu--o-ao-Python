game_name = 'Fifa 23'
game_description = """
  Fifa 23 é um jogo de futebol
  desenvolvido pela EA Sports
  e que possibilita jogar localmente ou online
"""

# string[inicio:fim] - indice começa na posição 0 / indice final -1

# 1 - Busque toda string a partir da primeira posição
print(game_name[0:])

# 2 - Busque toda string até a última posição
print(game_name[:7]) 

# 3 - Busque toda string da terceira até a últime posição
print(game_name[2:])

'''
string[inicio:fim:passo] - indice começa na posição 0 / indice final -1
passo - determina o incremento. Por padrão esse número é o 1
'''

# 4 - Busque toda a string de 2 em 2 caracteres
print(game_name[::2])

# Inverta uma string de trás pra frente
print(game_name[::-1])

# 5 - BUsque toda a string nos índices ímpares
print(game_name[1::2])