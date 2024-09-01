import tkinter as tk
import random
import string

def gerar_senha(tamanho, incluir_maiusculas, incluir_simbolos):
    caracteres = string.ascii_lowercase
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_simbolos:
        caracteres += string.punctuation

    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def gerar_senha_evento():
    try:
        tamanho = int(entry_tamanho.get())
        incluir_maiusculas = var_maiusculas.get()
        incluir_simbolos = var_simbolos.get()
        senha = gerar_senha(tamanho, incluir_maiusculas, incluir_simbolos)
        label_resultado.config(text=f"Senha gerada: {senha}")
        root.clipboard_clear()
        root.clipboard_append(senha)
        root.update()  # Atualiza o conteúdo da área de transferência
    except ValueError:
        label_resultado.config(text="Por favor, insira um número válido")

def copiar_senha_evento():
    try:
        senha = label_resultado.cget("text").replace("Senha gerada: ", "")
        if senha:
            root.clipboard_clear()
            root.clipboard_append(senha)
            root.update()
            label_resultado.config(text="Senha copiada para a área de transferência!")
        else:
            label_resultado.config(text="Nenhuma senha para copiar.")
    except Exception as e:
        label_resultado.config(text=f"Erro ao copiar: {e}")

# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de Senhas")

# Configuração do tamanho da fonte e cor de fundo
fonte_padrao = ('Arial', 12)
cor_fundo = '#f0f0f0'  # Cinza claro

root.configure(bg=cor_fundo)

# Frame principal para centralizar o conteúdo
frame = tk.Frame(root, bg=cor_fundo)
frame.pack(expand=True, fill='both')

# Frame interno para garantir a centralização
frame_interno = tk.Frame(frame, bg=cor_fundo)
frame_interno.pack(expand=True, fill='both')

# Criação dos widgets
label_tamanho = tk.Label(frame_interno, text="Informe o tamanho da senha:", font=fonte_padrao, bg=cor_fundo)
label_tamanho.pack(pady=10)

entry_tamanho = tk.Entry(frame_interno, font=fonte_padrao)
entry_tamanho.pack(pady=5)

var_maiusculas = tk.BooleanVar()
check_maiusculas = tk.Checkbutton(frame_interno, text="Incluir letras maiúsculas", variable=var_maiusculas, bg=cor_fundo, font=fonte_padrao)
check_maiusculas.pack(pady=5)

var_simbolos = tk.BooleanVar()
check_simbolos = tk.Checkbutton(frame_interno, text="Incluir símbolos", variable=var_simbolos, bg=cor_fundo, font=fonte_padrao)
check_simbolos.pack(pady=5)

button_gerar = tk.Button(frame_interno, text="Gerar Senha", command=gerar_senha_evento, font=fonte_padrao)
button_gerar.pack(pady=10)

button_copiar = tk.Button(frame_interno, text="Copiar Senha", command=copiar_senha_evento, font=fonte_padrao)
button_copiar.pack(pady=10)

label_resultado = tk.Label(frame_interno, text="", font=fonte_padrao, bg=cor_fundo)
label_resultado.pack(pady=10)

# Configuração da janela centralizada
largura_janela = 400
altura_janela = 300
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
x = (largura_tela - largura_janela) // 2
y = (altura_tela - altura_janela) // 2
root.geometry(f'{largura_janela}x{altura_janela}+{x}+{y}')

# Iniciar o loop da interface gráfica
root.mainloop()
