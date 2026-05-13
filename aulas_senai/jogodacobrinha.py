import tkinter as tk
import random

# Configurações
LARGURA = 600
ALTURA = 600
TAMANHO_CELULA = 20
VELOCIDADE = 120

# Cores
FUNDO = "#111111"
COBRA = "#00FF88"
COMIDA = "#FF3333"
TEXTO = "#FFFFFF"

# Janela principal
root = tk.Tk()
root.title("Jogo da Cobrinha")
root.resizable(False, False)

# Pontuação
pontuacao = 0

label_pontos = tk.Label(
    root,
    text=f"Pontuação: {pontuacao}",
    font=("Arial", 16, "bold"),
    fg=TEXTO,
    bg=FUNDO
)
label_pontos.pack(fill=tk.X)

# Canvas
canvas = tk.Canvas(
    root,
    width=LARGURA,
    height=ALTURA,
    bg=FUNDO,
    highlightthickness=0
)

canvas.pack()
canvas.focus_set()

# Cobra inicial
cobra = [
    [100, 100],
    [80, 100],
    [60, 100]
]

# Direção inicial
direcao = "Right"

# Comida
comida = [
    random.randint(0, (LARGURA // TAMANHO_CELULA) - 1) * TAMANHO_CELULA,
    random.randint(0, (ALTURA // TAMANHO_CELULA) - 1) * TAMANHO_CELULA
]


def desenhar():
    canvas.delete("all")

    # Desenha cobra
    for parte in cobra:
        x, y = parte

        canvas.create_rectangle(
            x,
            y,
            x + TAMANHO_CELULA,
            y + TAMANHO_CELULA,
            fill=COBRA,
            outline="#00cc6a"
        )

    # Desenha comida
    canvas.create_oval(
        comida[0],
        comida[1],
        comida[0] + TAMANHO_CELULA,
        comida[1] + TAMANHO_CELULA,
        fill=COMIDA,
        outline="#cc0000"
    )


def mover():
    global comida
    global pontuacao

    x, y = cobra[0]

    if direcao == "Up":
        y -= TAMANHO_CELULA

    elif direcao == "Down":
        y += TAMANHO_CELULA

    elif direcao == "Left":
        x -= TAMANHO_CELULA

    elif direcao == "Right":
        x += TAMANHO_CELULA

    nova_cabeca = [x, y]

    # Colisão com paredes
    if (
        x < 0 or
        x >= LARGURA or
        y < 0 or
        y >= ALTURA
    ):
        game_over()
        return

    # Colisão com o próprio corpo
    if nova_cabeca in cobra:
        game_over()
        return

    cobra.insert(0, nova_cabeca)

    # Comer comida
    if nova_cabeca == comida:

        pontuacao += 1

        label_pontos.config(
            text=f"Pontuação: {pontuacao}"
        )

        comida = [
            random.randint(0, (LARGURA // TAMANHO_CELULA) - 1) * TAMANHO_CELULA,
            random.randint(0, (ALTURA // TAMANHO_CELULA) - 1) * TAMANHO_CELULA
        ]

    else:
        cobra.pop()

    desenhar()

    root.after(VELOCIDADE, mover)


# Controle teclado
def mudar_direcao(event):
    global direcao

    nova = event.keysym

    if nova == "Up" and direcao != "Down":
        direcao = nova

    elif nova == "Down" and direcao != "Up":
        direcao = nova

    elif nova == "Left" and direcao != "Right":
        direcao = nova

    elif nova == "Right" and direcao != "Left":
        direcao = nova


# Tela de game over
def game_over():
    canvas.delete("all")

    canvas.create_text(
        LARGURA / 2,
        ALTURA / 2 - 20,
        text="GAME OVER",
        fill="#FF3333",
        font=("Arial", 32, "bold")
    )

    canvas.create_text(
        LARGURA / 2,
        ALTURA / 2 + 20,
        text=f"Pontuação final: {pontuacao}",
        fill=TEXTO,
        font=("Arial", 18)
    )


# Eventos
root.bind("<Key>", mudar_direcao)

# Iniciar jogo
desenhar()
mover()

# Loop principal
root.mainloop()
