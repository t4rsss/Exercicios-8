def entrada_segura():
    while True:
        try:
            num = int(input("Digite um número inteiro: "))
            print(f"O dobro do número é: {num * 2}")
            break
        except ValueError:
            print("Erro: Digite um número inteiro válido.")

entrada_segura()
