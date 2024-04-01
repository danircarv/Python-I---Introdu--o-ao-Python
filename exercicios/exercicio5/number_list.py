def check_even_odd(numbers):
    even = []
    odd = []
    
    for number in numbers:
        if number%2 == 0:
            even.append(number)
        elif number%2 ==1:
            odd.append(number)
        
    return even, odd
    

even_list, odd_list = check_even_odd([1,2,3,4,5,6,7,32,33,34,35])
print(f"Lista de números pares: {even_list}\n")
print(f"Lista de números ímpares: {odd_list}\n")  