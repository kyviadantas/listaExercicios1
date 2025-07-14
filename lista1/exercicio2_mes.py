mes = input("Digite o nome do mês: ").strip().lower()

meses = {
    "janeiro": 1, "fevereiro": 2, "março": 3, "abril": 4, "maio": 5, "junho":6,
    "julho":7, "agosto":8, "setembro":9, "outubro":10, "novembro":11, "dezembro":12
}

numero_mes = meses.get(mes)
if numero_mes:
    print(f"O mês {mes.capitalize()} corresponde ao número {numero_mes}.")
else:
    print("Mês inválido.")
