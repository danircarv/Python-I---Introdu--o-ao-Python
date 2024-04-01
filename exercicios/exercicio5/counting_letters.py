# Conta letras maiúsculas e minúsculas

# Escreva uma função Python que receba uma string e conte o número de letras maiúsculas e minúsculas desta string.

def check_char(frase):
    maiuscula = 0
    minuscula = 0
    
    for letra in frase:
        if letra.isupper():
            maiuscula += 1
        elif letra.islower():
            minuscula += 1
            
    return maiuscula, minuscula

phrase = input("Digite uma frase\n")
num_maiuscula, num_minuscula = check_char(phrase)
print(f"Existem {num_maiuscula} letras maiúsculas e {num_minuscula} letras minusculas na frase ")

    
