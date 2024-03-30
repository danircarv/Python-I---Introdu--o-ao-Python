name = input("Digite o nome do jogo\n")
launch_year = int(input("Digite o ano de lançamento do jogo\n"))
classification = float(input("Digite a nota de lançamento do jogo\n"))

if classification > 8.0 and launch_year > 2015:
  print(f"O jogo {name} é bom. Recomendo jogá-lo")
else:
  print(f"O jogo {name} ainda não atingiu uma boa nota. Por isso não recomendo.")