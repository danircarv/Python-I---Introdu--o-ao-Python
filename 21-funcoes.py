# 1 - Função para imprimir Hello World
def welcome():
    print("Hello World")
    
welcome()

# 2 - Função para somar dois números
def sum(num1,num2):
    return print(num1 + num2)

sum(1,3)

# 3 - Função para cadastrar um jogo
def create_game():
    name = input("Digite o nome do jogo\n")
    launch_year = int(input("Digite o ano de lançamento do jogo:\n"))
    game_price = float(input("Digite o preço do jogo:\n"))
    note_rating = (input("Digite a nota de avaliação do jogo\n"))
    print(f"{name} - R$ {game_price:.2f}")

create_game()