import pprint


games_dict = {
  "Resident Evil":{
    "launch_year": 2023,
    "classification":9.8,
    "genre": ["action", "adventure"]
  },
  "Mario":{
    "launch_year": 2017,
    "classification":10.0,
    "genre": ["adventure", "3d"]
  },
  "Donkey Kong":{
    "launch_year": 1995,
    "classification":9.5,
    "genre": ["adventure", "plataform"]
  } 
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(games_dict)

# 1 - Buscar informação de um dicionário aninhado
print(games_dict["Mario"]["genre"])

# 2 - Adicionar novo item
games_dict["Mario"]["players"] = 1
print(games_dict["Mario"])

# 3 - Excluir um dicionário
del games_dict["Resident Evil"]
pp.pprint(games_dict)