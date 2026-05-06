import tkinter as tk
from tkinter import ttk

def main():
    #Criação da janela "Pai"
    root = tk.Tk()
    root.title("Minha primeira janela")
    root.geometry("400x200")
    root.resizable(True,True)

    # lable simple (Etiqueta)
    label = ttk.Label(root, text="Jogo do dino", font=("TkDefaultFont", 16)) 
    label.pack(expand=True)

    # Botão para fechar a janela 
    
    btn = ttk.Button(root, text="fechar", command=root.destroy)
    btn.pack(anchor="center", pady=15) 

    # inicia o loop de eventos 
    root.mainloop()

if __name__ == "__main__":
    main()
