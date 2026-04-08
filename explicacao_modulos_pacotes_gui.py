import customtkinter



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


janela = customtkinter.CTk()
janela.geometry("400x300")

def click_login():
    print("clicou no login")

janela.title("Explicação de Modulos, Pacotes e GUI ❤👍")

texto = customtkinter.CTkLabel(janela, text="tela de fazer login")

email = customtkinter.CTkEntry(janela, placeholder_text="Digite seu email")


botao_login = customtkinter.CTkButton(janela, text="login", command=click_login)

texto.pack(pady=10)
email.pack(pady=10)
botao_login.pack(pady=10, padx=10)

janela.mainloop()

