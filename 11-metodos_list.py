games_list = ["Resident Evil", "Star Wars",
              "Zelda", "Red Dead", "Mario", "Luigi"]

# 1 - Tamanho da Lista
print(len(games_list))

# 2 - Recuperar um item da lista pelo índice
print(games_list.index("Mario"))

# 3 - Adicionar item ao final da lista
games_list.append("GTA")
print(games_list)

# 4 - Ordenar a lista
games_list.sort()
print(games_list)

# 5 - Copiar items de uma lista para outra
games_finished = games_list.copy()
games_finished.remove("Star Wars")
print(games_finished)

# 6 - Remove todos os itens da lista
games_list.clear()
print(games_list)