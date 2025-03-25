def divisao_segura():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 / num2
        except ValueError:
            print("Erro: Entrada inválida! Digite apenas números.")
        except ZeroDivisionError:
            print("Erro: Não é possível dividir por zero.")
        else:
            print(f"Resultado da divisão: {resultado}")
            break

divisao_segura()

