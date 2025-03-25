def abrir_arquivo():
    nome_arquivo = input("Digite o nome do arquivo: ")
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            print("Conteúdo do arquivo:\n", conteudo)
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

abrir_arquivo()
