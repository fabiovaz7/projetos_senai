import tkinter as tk

root = tk.Tk()
root.title("Itaú")
root.geometry("420x520")
root.configure(bg="#FF7200")

# impede redimensionamento
root.resizable(False, False)

# título
tk.Label(
    root,
    text="Itaú",
    font=("Arial", 40, "bold"),
    bg="#FF7200",
    fg="#FFFFFF"
).pack(pady=(10, 20))

tk.Label(
    root,
    text="Simulador de investimentos",
    font=("Arial", 12),
    bg="#FF7200",
    fg="#FFFFFF"
).pack(pady=(0, 25))

# Valor Inicial
tk.Label(
    root,
    text="Valor inicial (R$):",
    font=("Arial", 10, "bold"),
    bg="#FF7200",
    fg="#FFFFFF"
).pack(anchor="w", padx=20)

entrada_principal = tk.Entry(
    root,
    font=("Arial", 11),
    bg="#FFFFFF",
    fg="#FF7200",
    relief="groove"
)

entrada_principal.pack(
    pady=(4, 12),
    padx=20,
    ipady=8,
    fill=tk.X
)

# Taxa de juros
tk.Label(
    root,
    text="Taxa de juros ao mês (%):",
    font=("Arial", 10, "bold"),
    bg="#FF7200",
    fg="#FFFFFF"
).pack(anchor="w", padx=20)

entrada_taxa = tk.Entry(
    root,
    font=("Arial", 11),
    bg="#FFFFFF",
    fg="#FF7200",
    relief="groove"
)

entrada_taxa.pack(
    pady=(4, 12),
    padx=20,
    ipady=8,
    fill=tk.X
)

# Tempo em meses
tk.Label(
    root,
    text="Tempo em meses:",
    font=("Arial", 10, "bold"),
    bg="#FF7200",
    fg="#FFFFFF"
).pack(anchor="w", padx=20)

entrada_tempo = tk.Entry(
    root,
    font=("Arial", 11),
    bg="#FFFFFF",
    fg="#FF7200",
    relief="groove"
)

entrada_tempo.pack(
    pady=(4, 12),
    padx=20,
    ipady=8,
    fill=tk.X
)

# Label de resultado
lbl_resultado = tk.Label(
    root,
    text="Montante Final",
    font=("Arial", 14, "bold"),
    bg="#FF7200",
    fg="#FFFFFF",
    pady=12,
    relief=tk.FLAT
)

lbl_resultado.pack(fill=tk.X, padx=40, pady=(0, 16))

# Label de erro
lbl_erro = tk.Label(
    root,
    text="",
    font=("Arial", 9),
    bg="#FF7200",
    fg="#FFFFFF",
    pady=12,
    relief=tk.FLAT
)

lbl_erro.pack()

# Função calcular 
def calcular():
    lbl_erro.config(text="")

    try:
        principal = float(entrada_principal.get().replace(",", "."))
        taxa = float(entrada_taxa.get().replace(",", "."))
        tempo = int(entrada_tempo.get())

        montante = principal * (1 + taxa / 100) ** tempo

        lbl_resultado.config(
            text=f"Montante final: R$ {montante:.2f}"
        )

    except ValueError:
        lbl_erro.config(
            text="Preencha todos os campos corretamente."
        )

        lbl_resultado.config(
            text="Montante final: R$ -"
        )

# Botão calcular
btn_calcular = tk.Button(
    root,
    text="Calcular",
    font=("Arial", 11, "bold"),
    bg="#FF7200",
    fg="#FFFFFF",
    activebackground="#140083",
    activeforeground="#FFFFFF",
    relief=tk.FLAT,
    cursor="hand2",
    command=calcular
)

btn_calcular.pack(
    pady=10,
    padx=40,
    ipady=8,
    fill=tk.X
)

# efeito hover
def entrar_botao(e):
    btn_calcular.config(bg="#cc5c00")

def sair_botao(e):
    btn_calcular.config(bg="#FF7200")

btn_calcular.bind("<Enter>", entrar_botao)
btn_calcular.bind("<Leave>", sair_botao)

root.mainloop()
