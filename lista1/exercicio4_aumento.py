salario = float(input("Informe o salário atual: R$ "))

if 1500 <= salario < 1750:
    aumento_percentual = 12
elif 1750 <= salario < 2000:
    aumento_percentual = 10
elif 2000 <= salario < 3000:
    aumento_percentual = 7
elif salario >= 3000:
    aumento_percentual = 5
else:
    aumento_percentual = 15

valor_aumento = salario * (aumento_percentual / 100)
novo_salario = salario + valor_aumento

print(f"Aumento de {aumento_percentual}%. Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
