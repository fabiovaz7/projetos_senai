import tkinter as tk
import random

# Configurações
simbolos = ["🍌", "🍇", "🍉", "🍓", "🍊"]
saldo = 20.0
custo_giro = 2

# Função girar
def girar():
    global saldo

    if saldo < custo_giro:
        resultado_label.config(text="Saldo insuficiente", fg="red")
        return

    saldo -= custo_giro

    resultado = [random.choice(simbolos) for _ in range(3)]

    # Atualizando os slots
    slot1.config(text=resultado[0])
    slot2.config(text=resultado[1])
    slot3.config(text=resultado[2])

    # Verificando vitória
    if resultado[0] == resultado[1] == resultado[2]:
        saldo += 10
        resultado_label.config(text="🎉 Você ganhou!", fg="green")
    else:
        resultado_label.config(text="Tente novamente!", fg="black")

    saldo_label.config(text=f"Saldo: R$ {saldo:.2f}")

# Janela
janela = tk.Tk()
janela.title("FV BET")
janela.geometry("350x250")

# Título
titulo = tk.Label(janela, text="FV BET", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# Frame dos slots
frame_slots = tk.Frame(janela)
frame_slots.pack(pady=10)

# Slots (agora dentro do frame)
slot1 = tk.Label(frame_slots, text="❔", font=("Arial", 40))
slot1.pack(side="left", padx=10)

slot2 = tk.Label(frame_slots, text="❔", font=("Arial", 40))
slot2.pack(side="left", padx=10)

slot3 = tk.Label(frame_slots, text="❔", font=("Arial", 40))
slot3.pack(side="left", padx=10)

# Botão girar
botao = tk.Button(janela, text="Girar", command=girar)
botao.pack(pady=10)

# Resultado
resultado_label = tk.Label(janela, text="Clique para girar")
resultado_label.pack()

# Saldo
saldo_label = tk.Label(janela, text=f"Saldo: R$ {saldo:.2f}", font=("Arial", 12))
saldo_label.pack(pady=5)

janela.mainloop()

