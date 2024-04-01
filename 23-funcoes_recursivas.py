def factorial(num):
    if num == 1:
        return 1
    else:
        return(num * factorial(num - 1))
    
number = int(input("Digite o numero para o fatorial\n"))
print(f"O fatorial de {number} é: {factorial(number)}")

# 2 - Soma dos numeros naturais de 0 até n
def total_sum(num):
    if num == 1:
        return 1
    else:
        return(num + total_sum(num - 1))
    
num = int(input("Digite o número para a soma\n"))
print(f"A soma total dos naturais de 0 até {num} é {total_sum(num)}")