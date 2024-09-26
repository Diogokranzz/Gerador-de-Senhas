from cryptography.fernet import Fernet

# Gera uma nova chave
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)
    print("Chave gerada e salva em 'chave.key'.")

if __name__ == "__main__":
    gerar_chave()