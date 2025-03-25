def operacao_bancaria():
    saldo = 1000.00
    try:
        saque = float(input("Digite o valor para saque: R$ "))
        if saque > saldo:
            print(f"Saldo insuficiente! Saldo disponível: R$ {saldo:.2f}")
        else:
            saldo -= saque
            print(f"Saque realizado com sucesso! Saldo restante: R$ {saldo:.2f}")
    except ValueError:
        print("Erro: Digite um valor numérico válido.")

operacao_bancaria()
