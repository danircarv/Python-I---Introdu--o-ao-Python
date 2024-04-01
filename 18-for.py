game_list = ["Fifa", "God of War", "Red Dead", "Uncharted"]



# 1 - Iterando valores de uma lista
for game in game_list:
    print(game)

print("----------------------------------")
    
# 2 - Quando a condição for atendida, o loop será encerrado
for game in game_list:
    if game == "Red Dead":
        break
    print(game)
    
print("----------------------------------")
    
# 3 - Quando a condição for atendida, o loop vai para a proxima iteração
for game in game_list:
    if game == "Red Dead":
        continue
    print(game)
    
print("----------------------------------")

# 4 - Avaliação do jogo
game_name = input("Digite o nome do jogo\n")
game_rating = int(input("Digite quantas avaliações deseja fazer no jogo\n"))

sum = 0
for i in range(game_rating):
    note = float(input("Qual a nota para o jogo\n"))
    sum += note # sum = sum + note
print(f"Média de avaliação do jogo {game_name} é {sum/game_rating :.2f} ")
    



