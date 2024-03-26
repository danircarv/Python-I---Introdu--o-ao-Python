name = input("Digite o nome do jogo\n")
launch_year = int(input("Digite o ano de lançamento do jogo:\n"))
game_price = float(input("Digite o preço do jogo:\n"))
plan_included = (input("Está incluso no serviço mensal?\n"))

print("###Dados do Jogo###")
print("===================")
# Alternativa 1
# print("Nome do jogo:", name)
# print("Ano do jogo:", launch_year)
# print("Preço do jogo:", game_price)
# print("Está incluído no plano?", plan_included)

# Alternativa 2
# print("Nome do jogo:", name, "\n Ano de lançamento:", launch_year,
#       "\n Preço do Jogo:", game_price, "\n Está incluso no serviço?", plan_included)

# Alternativa 3
print(f"Nome do jogo: {name} \nAno de lançamento: {launch_year} \nPreço do Jogo: {game_price} \nEstá incluso no serviço? {plan_included}")
