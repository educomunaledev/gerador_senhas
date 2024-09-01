import tkinter as tk
from tkinter import messagebox
import random
import string

def gerar_senha(comprimento, incluir_maiusculas, incluir_simbolos):
    caracteres = string.ascii_lowercase
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_simbolos:
        caracteres += string.punctuation
    caracteres += string.digits

    senha = ''.join(random.choice(caracteres) for i in range(comprimento))
    return senha

def gerar():
    try:
        comprimento = int(entry_comprimento.get())
        incluir_maiusculas = var_maiusculas.get()
        incluir_simbolos = var_simbolos.get()

        senha = gerar_senha(comprimento, incluir_maiusculas, incluir_simbolos)
        label_resultado.config(text=f"Senha gerada: {senha}")
    except ValueError:
        messagebox.showerror("Erro", "Comprimento da senha deve ser um número inteiro.")

# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de Senhas")

# Comprimento da senha
tk.Label(root, text="Comprimento da senha:").pack(pady=5)
entry_comprimento = tk.Entry(root)
entry_comprimento.pack(pady=5)

# Opções para incluir maiúsculas e símbolos
var_maiusculas = tk.BooleanVar()
tk.Checkbutton(root, text="Incluir letras maiúsculas", variable=var_maiusculas).pack(pady=5)

var_simbolos = tk.BooleanVar()
tk.Checkbutton(root, text="Incluir símbolos", variable=var_simbolos).pack(pady=5)

# Botão para gerar a senha
tk.Button(root, text="Gerar Senha", command=gerar).pack(pady=10)

# Label para exibir o resultado
label_resultado = tk.Label(root, text="Senha gerada:")
label_resultado.pack(pady=5)

# Iniciar a aplicação
root.mainloop()
