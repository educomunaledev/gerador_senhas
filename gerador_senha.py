import random
import string 

def gerar_senha(tamanho=8, incluir_letras=True, incluir_números=True, incluir_simbolos=True):
    caracteres = ''

    if incluir_letras:
        caracteres += string.ascii_letters
    if incluir_números:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        print("Nenhum tipo de caractere foi selecionado")

    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha 

if __name__ == "__main__":
    tamanho = int(input("Informe o tamanho da senha: "))
    senha =  gerar_senha(tamanho)
    print(f"Senha gerada: {senha}")
    
    


