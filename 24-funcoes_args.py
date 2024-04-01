"""
*args: Utilizamos ele quando não temos a certeza de quantos
argumentos vamos ter dentro de uma função. Ao utilizá-lo, 
deixamos essa informação dinâmica e variável.
- Os argumentos são passados como uma tupla.

**kwargs: Além dos valores, podemos passar também as respectivas
chaves para cada argumento.
- Os argumentos são passados como um dicionário.
"""

# 1 - Soma de números

from os import name
from unicodedata import category


def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"A soma dos números é: {sum_total}")

sum(7,9,3,4,5,6,7,5,6,3,5666,1345,664,56,2,1)


# 2 - Apresentação de cursos
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")

presentation(name="Python", category="Backend", level="Iniciante")
presentation(name="Visão Computacional com Python", category="IA", level="Avançado")
presentation(name="Dashboards com Dash", category="Data Science", level="Intermediário")