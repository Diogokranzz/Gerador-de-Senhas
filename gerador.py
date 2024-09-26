import random
import string

class GeradorDeSenhas:
    def __init__(self, tamanho=12, incluir_simbolos=True):
        self.tamanho = tamanho
        self.incluir_simbolos = incluir_simbolos

    def gerar(self):
        caracteres = string.ascii_letters + string.digits
        if self.incluir_simbolos:
            caracteres += string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(self.tamanho))
        return senha

def obter_tamanho_senha():
    while True:
        try:
            tamanho = int(input("Digite o tamanho da senha (padrão 12): ") or 12)
            if tamanho <= 0:
                raise ValueError
            return tamanho
        except ValueError:
            print("Por favor, insira um número válido.")

if __name__ == "__main__":
    tamanho = obter_tamanho_senha()
    incluir_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'
    gerador = GeradorDeSenhas(tamanho, incluir_simbolos)
    senha_gerada = gerador.gerar()
    print(f"Sua senha gerada é: {senha_gerada}")