game_fifa = {
    "name": "Fifa 23",
    "year_launch": 2022,
    "game_price": 90.50,
    "classification": 8.5,
    "genre": ["sport","family"]
}         

print(game_fifa)
print(len(game_fifa))
print(type(game_fifa))

# 1 - Recuperar um elemento do dicionario
print(game_fifa['genre'])
print(game_fifa.get("classification"))

# 2 - Buscar apenas as chaves do dicionario
print(game_fifa.keys())

# 3 - Buscar apenas os valores do dicionario
print(game_fifa.values())

# 4 - Buscar itens do dicionario com chaves e valor
print(game_fifa.items())

# 5 - Adicionar itens no dicionario
game_fifa['players'] = 2
print(game_fifa)

# 6 - Atualizar itens no dicionario
game_fifa.update({"players": 1})
print(game_fifa)

# 7 - Remover item do dicionario
game_fifa.pop("players")
print(game_fifa)