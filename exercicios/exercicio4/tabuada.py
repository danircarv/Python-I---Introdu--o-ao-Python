print("TABUADA")
number = int(input("Qual o número que você deseja saber a tabuada\n"))
initial_num = int(input("Valor inicial da tabuada:\n"))
final_num = int(input("Valor final da tabuada:\n"))

for i in range(initial_num,final_num):
    print(f"{number} x {i} = {number*i}")
    