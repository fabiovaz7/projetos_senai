import tkinter as tk
from tkinter import messagebox

# Funções da calculadora

def adicionar(valor):
    display.insert(tk.END, valor)

def limpar():
    display.delete(0, tk.END)

def calcular():
    try:
        expressao = display.get()

        # Substituição de símbolos
        expressao = expressao.replace('X', '*').replace('÷', '/')

        resultado = eval(expressao)

        display.delete(0, tk.END)
        display.insert(tk.END, resultado)

    except ZeroDivisionError:
        messagebox.showerror("Erro", "Divisão por zero!")
        limpar()

    except:
        messagebox.showerror("Erro", "Expressão inválida!")
        limpar()


# Interface
janela = tk.Tk()
janela.title("Calculadora FV")
janela.geometry("360x500")
janela.resizable(width=False, height=False)

# Display
display = tk.Entry(
    janela,
    font=("Arial", 24),
    justify="right",
    bd=10,
    relief="sunken"
)

display.grid(
    column=0,
    row=0,
    columnspan=4,
    padx=10,
    pady=20,
    ipadx=8,
    ipady=20
)

# Lista de botões
botoes = [
    'C', '±', '%', '÷',
    '7', '8', '9', 'X',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '0', '.', '='
]

# Cores
cor_numero = "#ffffff"
cor_operador = "#ff9500"
cor_especial = "#a6a6a6"

# Criação dos botões
row = 1
col = 0

for botao in botoes:

    if botao == "=":
        btn = tk.Button(
            janela,
            text=botao,
            font=("Arial", 24, "bold"),
            bg=cor_operador,
            fg="white",
            command=calcular
        )

        btn.grid(
            column=col,
            row=row,
            columnspan=2,
            padx=3,
            pady=3,
            sticky="nsew"
        )

        col += 2

    elif botao == "0":
        btn = tk.Button(
            janela,
            text=botao,
            font=("Arial", 24),
            bg=cor_numero,
            command=lambda v=botao: adicionar(v)
        )

        btn.grid(
            column=col,
            row=row,
            columnspan=2,
            padx=3,
            pady=3,
            sticky="nsew"
        )

        col += 2

    else:

        if botao in ["C", "±", "%"]:
            cor = cor_especial
        elif botao in ["÷", "X", "-", "+"]:
            cor = cor_operador
        else:
            cor = cor_numero

        if botao == "C":
            comando = limpar
        else:
            comando = lambda v=botao: adicionar(v)

        btn = tk.Button(
            janela,
            text=botao,
            font=("Arial", 24),
            bg=cor,
            command=comando
        )

        btn.grid(
            column=col,
            row=row,
            padx=3,
            pady=3,
            sticky="nsew"
        )

        col += 1

    if col > 3:
        col = 0
        row += 1

# Faz os botões expandirem
for i in range(6):
    janela.grid_rowconfigure(i, weight=1)

for i in range(4):
    janela.grid_columnconfigure(i, weight=1)

janela.mainloop()