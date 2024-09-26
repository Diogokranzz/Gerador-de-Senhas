import json
import os
from cryptography.fernet import Fernet

class GerenciadorDeSenhas:
    def __init__(self, key):
        self.key = key
        self.fernet = Fernet(key)

    def salvar_senha(self, nome, senha):
        senha_encriptada = self.fernet.encrypt(senha.encode())
        if not os.path.exists('senhas.json'):
            with open('senhas.json', 'w') as f:
                json.dump({}, f)

        with open('senhas.json', 'r+') as f:
            senhas = json.load(f)
            if nome in senhas:
                print("Uma senha com esse nome já existe. Escolha um nome diferente.")
                return
            senhas[nome] = senha_encriptada.decode()
            f.seek(0)
            json.dump(senhas, f, indent=4)
            f.truncate()

    def listar_senhas(self):
        if os.path.exists('senhas.json'):
            with open('senhas.json', 'r') as f:
                senhas = json.load(f)
                for nome, senha in senhas.items():
                    senha_decriptada = self.fernet.decrypt(senha.encode()).decode()
                    print(f"{nome}: {senha_decriptada}")
        else:
            print("Nenhuma senha salva.")

def main():
    key = b'tUqv9qmnlvmuIxnVvoCZOGvDUV54jmtp41kPr5pAFxM='  # Substitua pela chave gerada
    gerenciador = GerenciadorDeSenhas(key)

    while True:
        acao = input("\nEscolha uma ação:\n1. Salvar senha\n2. Listar senhas\n3. Sair\n> ").strip()

        if acao == '1':
            nome = input("Nome do serviço: ")
            senha = input("Senha: ")
            gerenciador.salvar_senha(nome, senha)
            print("Senha salva com sucesso!")
        
        elif acao == '2':
            gerenciador.listar_senhas()
        
        elif acao == '3':
            break
        
        else:
            print("Ação inválida. Tente novamente.")

if __name__ == "__main__":
    main()