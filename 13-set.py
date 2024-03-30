game_set = {"Fifa 23", "Red Dead", "Star Wars", "Zelda",
            "Mario", "Resident Evil"}
print(game_set)

# 1 - Buscar o tamanho do set
print(len(game_set))

# 2 - True e 1 são considerados o mesmo valor
example_set = {"Fifa 23", True, 1, 90.50}
print(example_set)

# 3 - Adicionar item de outro set
game_set.update(example_set)
print(game_set)

# 4 - Remover um item do set
game_set.remove(True)
game_set.remove(90.50)
print(game_set)









# - Não possibilita recuperar valores via slice

