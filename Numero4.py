def acessar_lista():
    numeros = [10, 20, 30, 40, 50]
    while True:
        try:
            indice = int(input(f"Digite um índice entre 0 e {len(numeros) - 1}: "))
            print(f"O valor no índice {indice} é {numeros[indice]}")
            break
        except ValueError:
            print("Erro: Digite um número inteiro.")
        except IndexError:
            print(f"Erro: Índice fora do intervalo. Digite um valor entre 0 e {len(numeros) - 1}.")

acessar_lista()
