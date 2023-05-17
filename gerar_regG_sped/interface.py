import tkinter as tk
from tkinter import ttk
import gerar_regg
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import modificar_sped


class Single_window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Gerador CIAP SPED')
        self.state('zoomed')


def mensagem_exporta():
    messagebox.showinfo("Exportar txt", "Arquivo Gerado com Sucesso !")

def mensagem_importa():
    messagebox.showinfo("Importação", "Planilha importada com Sucesso !!")

def mensagem_sped_atualizado():
        messagebox.showinfo("Registros atualizados no SPED EFD !!")


root = Single_window()
title_app = tk.Frame(root)
space_0 = ttk.Label(title_app,text="\n                                                                                  "
                                   "                                                                                    "
                                   "                                                          Menu Principal\n"
                                   " _________________________________________________________________________"
                                   "______________________________________________________________________________________________"
                                   "____________________________________________",width=6007, padding=5, font= "Arial 12", foreground="#a19f9f")
space_0.grid(row=0,column=0)
title_app.pack(side = 'top')


title_app = tk.Frame(root)
space_0 = ttk.Label(title_app,text="",width=6007, padding=15, font= "Arial 12")
space_0.grid(row=0,column=0)
title_app.pack(side = 'top')


msg1 = "Importar Relatorio CIAP".format("bold")
msg3 = "Exportar REG G"
msg30 = "Exportar 0300"



button_f3 = tk.Frame(root)



space_3 = PanedWindow(button_f3,width=100,height=30,background="#cacbd2")
space_3.grid(row=10, column=1, columnspan=10)

button_10 = Button(button_f3, text = '\n IRC \n',bg="#4040ff",width=21, pady=60,padx=10, border=2,font='arial 16',foreground='#cacbd2')
button_10.grid(row=4, column=0)
button_10["command"] = lambda:[gerar_regg.deleta_dados_antigos(),gerar_regg.importa_relatorio(),mensagem_importa()]

space_3 = PanedWindow(button_f3,width=100,height=30,background="#cacbd2")
space_3.grid(row=10, column=1, columnspan=1)

button_12 = Button(button_f3, text = '\n ERG \n ',bg="#4040ff",width=21, pady=60,padx=10, border=2,font='arial 16',foreground='#cacbd2')
button_12.grid(row=4, column=2)
button_f3.pack(side = 'top')
button_12["command"] = lambda:[gerar_regg.gerar_registro_g(),mensagem_exporta()]

space_3 = PanedWindow(button_f3,width=100,height=30,background="#cacbd2")
space_3.grid(row=3, column=3,)

button_13 = Button(button_f3, text = '\n ER3 \n ',bg="#4040ff",width=21, pady=60,padx=10, border=2,font='arial 16',foreground='#cacbd2')
button_13.grid(row=4, column=4)
button_f3.pack(side = 'top')
button_13["command"] = lambda:[gerar_regg.gerar_300_305(),mensagem_exporta()]

space_4 = PanedWindow(button_f3,width=100,height=30,background="#cacbd2")
space_4.grid(row=5, column=2,)

button_11 = Button(button_f3, text = '\n Exportar SPED \n ',bg="#4040ff",width=21, pady=12,padx=5, border=2,font='arial 18',foreground='#cacbd2')
button_11.grid(row=6, column=2)
button_f3.pack(side = 'top')
button_11["command"] = lambda:[modificar_sped.importa_sped(),modificar_sped.encontrar_linha_registro_sped(),modificar_sped.adicionar_frase_texto(),
                               modificar_sped.encontrar_linha_registro_sped_300(),modificar_sped.adicionar_frase_texto_300(),mensagem_sped_atualizado()]


def on_enter(event):
    button_11.config(bg="blue", fg="white")

def on_leave(event):
    button_11.config(bg="#4040ff", fg="#cacbd2")

button_11.bind("<Enter>", on_enter)
button_11.bind("<Leave>", on_leave)

def on_enter(event):
    button_10.config(bg="blue", fg="white")

def on_leave(event):
    button_10.config(bg="#4040ff", fg="#cacbd2")

button_10.bind("<Enter>", on_enter)
button_10.bind("<Leave>", on_leave)

def on_enter(event):
    button_12.config(bg="blue", fg="white")

def on_leave(event):
    button_12.config(bg="#4040ff", fg="#cacbd2")

button_12.bind("<Enter>", on_enter)
button_12.bind("<Leave>", on_leave)

def on_enter(event):
    button_13.config(bg="blue", fg="white")

def on_leave(event):
    button_13.config(bg="#4040ff", fg="#cacbd2")

button_13.bind("<Enter>", on_enter)
button_13.bind("<Leave>", on_leave)






button_f3.configure(background="#cacbd2")
root.configure(background="#cacbd2")

root.mainloop()





