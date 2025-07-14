homens = int(input("Informe a quantidade de homens: "))
mulheres = int(input("Informe a quantidade de mulheres: "))
total = homens + mulheres

opcao = int(input("Digite 1 para percentual de mulheres ou 2 para percentual de homens: "))

if opcao == 1:
    percentual = (mulheres / total) * 100
    print(f"Percentual de mulheres: {percentual:.2f}%")
elif opcao == 2:
    percentual = (homens / total) * 100
    print(f"Percentual de homens: {percentual:.2f}%")
else:
    print("Opção inválida.")
