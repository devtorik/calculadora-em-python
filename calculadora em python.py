# Funções para as operações básicas
def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b


# Função principal da calculadora
def calculadora():
    while True:
        # Exibir um menu para escolha da operação
        print("\nBem-vindo à Calculadora!")
        print("Escolha uma operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        # Obter a escolha do usuário
        opcao = input("Digite o número da operação (1-5): ")

        # Se o usuário quiser sair, encerre o loop
        if opcao == "5":
            print("Obrigado por usar a calculadora!")
            break

        # Verificar se a escolha é válida
        if opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida. Tente novamente.")
            continue

        # Obter os valores de entrada do usuário
        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))

            # Executar a operação correspondente
            if opcao == "1":
                resultado = adicionar(a, b)
                operacao = "+"
            elif opcao == "2":
                resultado = subtrair(a, b)
                operacao = "-"
            elif opcao == "3":
                resultado = multiplicar(a, b)
                operacao = "*"
            elif opcao == "4":
                resultado = dividir(a, b)
                operacao = "/"

            # Exibir o resultado
            print(f"Resultado: {a} {operacao} {b} = {resultado}")

        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")
        except Exception as e:
            print(f"Erro: {e}. Tente novamente.")


# Chamar a função da calculadora para iniciar
calculadora()
