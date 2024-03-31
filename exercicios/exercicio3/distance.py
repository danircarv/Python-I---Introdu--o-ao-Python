def calc_price(distance):
  if distance < 200:
    price = 0.5*distance
    print(f"O preço a ser pago é {price:.2f}")
  else:
    price = 0.35*distance
    print(f"O preço a ser pago é {price:.2f}")

distancia = float(input("Qual a distância, em km, que você deseja percorrer?\n"))
calc_price(distancia)