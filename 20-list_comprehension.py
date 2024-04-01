# 1 - liste valores de 0 a 10 que sejam menor do que 4
# for i in range(10):
#     if i<4:
#         print(i)
list_numbers = [i for i in range(10) if i<4]
print(list_numbers)

games_list = ["Mario", "Donkey King",
              "Luigi", "Kirby"]

# 2 - Jogos que possuas a letra a 
new_list = [x for x in games_list if "a" in x]
print(new_list)

# 3 - Jogos que eu gerei
games_finished = [x for x in games_list if x != "Kirby"]
print(games_finished)

