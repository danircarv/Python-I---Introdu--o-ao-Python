# 1 - Cire uma função que receba dois argumentos: o primeiro nome e o segundo nome
def full_name(fname, lname):
    print(f"Nome completo: {fname} {lname}")
    
full_name("Daniel", "Carvalho")

# 2 - Crie uma função que some dois numeros via parametros
def sum(a,b):
    return a + b

print(sum(1,10))

# 3 - Argumentos default numa função
def address(country="Brasil"):
    print(f"Eu moro no {country}")
    
address() 
address("Espanha")

# 4 - Avaliação do jogo
def rating_game(qtdRating):
    game_name = input("Digite o nome do jogo\n")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota para o jogo\n"))
        sum += note
    print(f"Média da avaliação o jogo {game_name}: {sum/ qtdRating}")
    
rating_game(2)
    

    
