import time

def menu():
    while True:
        print("\nEscolha um programa para executar: \n ")
        print("1 - Calcular débito")
        print("2 - Calcular data")
        print("3 - Sair")

        opcao = input("Digite: ")

        if opcao == '1':
            calcular_debito()
        elif opcao == '2':
            calcular_data()
        elif opcao == '3':
            print("Programa encerrado.")
            break  
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")
            
def calcular_debito():

    debito = input("\nInforme do débito para calcular: ")
    debito = debito.replace(",", ".")

    try:
        debito = float(debito)
    except ValueError:
        print("Por favor, digite um número válido.")
        exit()

    print("\nEscolha a opção de desconto: \n")
    print("A - 1 x1,9 + 5 x9,9")
    print("B - 6 x 9,9")
    print("C - 3 x1,9 + 3 x9,9")

    descontos = {"x": 1.9, "y": 9.9}

    escolha = input("\nDigite a letra da opção escolhida: ").lower()

    try:
        opcaop = int(input("Escolha a opção de parcelamento (de 1x a 6x): "))
        if opcaop < 1 or opcaop > 6:
            print("Escolha um número entre 1 e 6.")
            exit()
    except ValueError:
        print("Digite um número inteiro válido para o parcelamento.")
        exit()

    print(f"Você escolheu parcelar {opcaop}x")
    print(f"\nCalculando...")
    
    time.sleep(2)

    razao = round (debito / opcaop, 2)
    i = 1  

    if escolha == 'a':
        print(f"{i}ª parcela: {razao + descontos['x']}")
        i+=1
        while i <= opcaop:
            print(f"{i}ª parcela: {razao + descontos['y']}")
            i += 1
        while i > opcaop and i <= 6:
            print(f"{i}ª parcela: {descontos['y']}")
            i+=1

    elif escolha == 'b':
        while i <= opcaop:
            print(f"{i}ª parcela: {razao + descontos['y']}")
            i += 1
        while i > opcaop and i <= 6:
            print(f"{i}ª parcela: {descontos['y']}")
            i+=1

    elif escolha == 'c':
        while i <= opcaop // 2:
            print(f"{i+1}ª parcela: {razao + descontos['x']}")
            i += 1
        while i < opcaop:
            print(f"{i+1}ª parcela: {razao + descontos['y']}")
            i += 1

    else:
        print("Digite uma opção válida.")

    time.sleep(3)

def calcular_data():
    
    from datetime import datetime, timedelta

    hoje = datetime.today()
    
    hoje = datetime.today()
    dias_opcoes = {"a": 9, "b": 23, "c": 14}

    print("Escolha uma opção:")
    print("a - Boleto Digital")
    print("b - Boleto Impresso")
    print("c - CC e DC")
    print("d - Regra de boleto")

    opcao = input("\n Digite a opção desejada: ").lower()

    if opcao in dias_opcoes:
        dias_somar = dias_opcoes[opcao] 
        nova_data = hoje + timedelta(days=dias_somar)
        print(f"A nova data após somar {dias_somar + 1} dias será: {nova_data.strftime('%d/%m/%Y')}")

    elif opcao == 'd': 
        nova_data = hoje - timedelta(60)
        print(f"A data atual menos 60 dias é: {nova_data.strftime('%d/%m/%Y')}")
    
    else:
        print("Opção inválida. Escolha 'a', 'b', 'c' ou 'd'.")

    time.sleep(3)

menu()
