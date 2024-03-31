def raise_salary(salary):
  if salary>1250:
    bonus = 0.1*salary
    print(f"O aumento é {bonus:.2f}")
  else: 
    bonus = 0.15*salary
    print(f"O aumento é {bonus:.2f}")
    
salario = float(input("Digite seu salário atual para descobrir seu aumento\n"))
raise_salary(salario)