import tkinter as tk
from tkinter import messagebox


total_cadastrados = 0
total_em_dia = 0

EPIS_POR_SETOR = {
    "1": ("Elétrica", "Luvas de alta tensão e botas dielétricas."),
    "2": ("Trabalho em Altura", "Cinturão de segurança e talabarte.")
}


def cadastrar():
    global total_cadastrados, total_em_dia
    

    nome = caixa_nome.get()
    opcao_setor = caixa_setor.get()
    nr10 = caixa_nr10.get().upper()
    nr35 = caixa_nr35.get().upper()
    

    try:
        ano_brigada = int(caixa_ano.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números no ano!")
        return

    total_cadastrados += 1


    setor, epis = EPIS_POR_SETOR.get(opcao_setor, ("Outro", "Consultar setor de segurança."))
    

    brigada_ok = False
    if (2026 - ano_brigada) <= 2:
        brigada_ok = True
        msg_brigada = "Válido"
    else:
        msg_brigada = "Vencido! Fazer reciclagem."


    if nr10 == "OK" and nr35 == "OK" and brigada_ok:
        total_em_dia += 1


    resultado = f"Setor: {setor}\nEPIs: {epis}\nBrigada: {msg_brigada}"
    messagebox.showinfo(f"Resultado - {nome}", resultado)

    caixa_nome.delete(0, tk.END)
    caixa_setor.delete(0, tk.END)
    caixa_nr10.delete(0, tk.END)
    caixa_nr35.delete(0, tk.END)
    caixa_ano.delete(0, tk.END)

def relatorio():
    texto = f"Total cadastrados: {total_cadastrados}\nTotal de pessoas em dia: {total_em_dia}"
    messagebox.showinfo("Relatório Final", texto)



janela = tk.Tk()
janela.title("senaizin")
janela.geometry("500x550")
janela.config(bg="#392b53")


tk.Label(janela, text="Nome do funcionário:", bg="#392b53", fg="white", font=("Aptos Black", 14, "bold")).pack(pady=15)
caixa_nome = tk.Entry(janela, font=("Arial", 14, "bold"), justify="center")
caixa_nome.pack()

tk.Label(janela, text="Setor (1-Elétrica, 2-Altura, Outro):", bg="#392b53", fg="white", font=("Aptos Black", 14, "bold")).pack(pady=5)
caixa_setor = tk.Entry(janela, font=("Arial", 14, "bold"), justify="center")
caixa_setor.pack()

tk.Label(janela, text="Status NR-10 (OK ou Pendente):", bg="#392b53", fg="white", font=("Aptos Black", 14, "bold")).pack(pady=5)
caixa_nr10 = tk.Entry(janela, font=("Arial", 14, "bold"), justify="center")
caixa_nr10.pack()

tk.Label(janela, text="Status NR-35 (OK ou Pendente):", bg="#392b53", fg="white", font=("Aptos Black", 14, "bold")).pack(pady=5)
caixa_nr35 = tk.Entry(janela, font=("Arial", 14, "bold"), justify="center")
caixa_nr35.pack()

tk.Label(janela, text="Ano Treinamento Brigada:", bg="#392b53", fg="white", font=("Aptos Black", 14, "bold")).pack(pady=5)
caixa_ano = tk.Entry(janela, font=("Arial", 14, "bold"), justify="center")
caixa_ano.pack()


tk.Button(janela, text="Cadastrar", command=cadastrar, bg="#53c51e", width=15, height=1, font=("Aptos Black", 14, "bold")).pack(pady=15)
tk.Button(janela, text="Ver Relatório Final", command=relatorio, bg="#9dabf7", width=15, height=1, font=("Aptos Black", 14, "bold")).pack()
tk.Button(janela, text="Fechar", command=janela.destroy, bg="#c71313", width=15, height=1, font=("Aptos Black", 14, "bold")).pack(pady=15)



janela.mainloop()