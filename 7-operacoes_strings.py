game_description = """
  Fifa 23 é um jogo de futebol
  desenvolvido pela EA Sports
  e que possibilita jogar localmente ou online
"""

game_name = 'Fifa'
game_version = ' 23'
line = "="


# 1 - Operação de Concatenação de Strings 
print(line * 25)
game_fullname = game_name + game_version
print(game_fullname)

# 2 - Operação de multiplicação de Strings

print(line * 25)

# 3 - Procura palavra dentro de um texto
print("Fifa" in game_description)
print("futebol" in game_description)

