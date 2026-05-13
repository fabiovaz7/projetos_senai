import tkinter as tk

root = tk.Tk()
root.title("Simulador de investimentos - Sicredi")
root.geometry("400x420")
root.configure(bg="#005c36")

# impede redimensionamento
root.resizable(False, False)

# título
tk.Label(
    root,
    text="=== Simulador de Investimentos ===",
    font=("Arial", 10, "italic"),
    bg="#005c36",
    fg="#a8d5bc"
).pack(pady=(10, 20))

# Valor Inicial
tk.Label(
    root,
    text="Valor inicial (R$):",
    font=("Arial", 10, "bold"),
    bg="#005c36",
    fg="#FFFFFF"
).pack(anchor="w", padx=20)

entrada_principal = tk.Entry(
    root,
    font=("Arial", 11),
    bg="#FFFFFF",
    fg="#005c36",
    relief="groove",
    width=40
)

entrada_principal.pack(pady = (4, 12), ipadx = 6, ipady = 8, fill = tk.X)

root.mainloop()

On Wed, Apr 15, 2026 at 4:27 PM Fabio Vaz <fabinhoaugustovaz@gmail.com> wrote:

