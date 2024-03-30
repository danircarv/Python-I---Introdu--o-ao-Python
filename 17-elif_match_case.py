num1 = float(input("Digite o número 1\n"))
num2 = float(input("Digite o número 2\n"))
operation = int(input("Digite a operação a realizar:\n 1-Soma\n 2-Subtração\n 3-Multiplicação\n 4-Divisão\n"))

if operation == 1:
  result = num1 + num2
elif operation == 2:
  result = num1 - num2
elif operation == 3:
  result = num1*num2
elif operation ==4:
  result = num1/num2
else:
  print("Operação Inválida")
  result = None
print(f"Resultado é : {result:.2f}")

print("Fazendo agora com match-case...")
num2 = float(input("Digite o número 1\n"))
num3 = float(input("Digite o número 2\n"))
operation_1 = int(input("Digite a operação a realizar:\n 1-Soma\n 2-Subtração\n 3-Multiplicação\n 4-Divisão\n"))

match operation_1:
    case 1:
        result_1 = num2 + num3
    case 2:
        result_1 = num2 - num3
    case 3:
        result_1 = num2 * num3
    case 4:
        result_1 = num2 / num3
    case _:
      print("Opção inválida!")
print(f"O Resultado dessa operação como match-case é {result_1:.3f}")


