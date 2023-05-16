import sqlite3
from tkinter import filedialog
import pandas as pd

conexao = sqlite3.connect('reg_g.db')
cursor = conexao.cursor()

def deleta_dados_antigos():
    deleta_dados_tabela = 'delete from reg_g'
    cursor.execute(deleta_dados_tabela)
    conexao.commit()


def importa_relatorio():
    filename_saida = filedialog.askopenfilename(initialdir="/home", title="Select a File",
                                                    filetypes=(("Text files", "*.*"), ("all files", "*.*")))
    wb1 = pd.read_excel(filename_saida, sheet_name='reg_g')
    wb1.to_sql(name='reg_g', con=conexao, if_exists='append', index=False)


def gerar_registro_g():
    consulta = 'SELECT * FROM reg_g'
    cursor.execute(consulta)
    with open('sped_reg_g.txt', 'w', encoding="utf8") as file:

        for linha in cursor.fetchall():
            if linha[7]==1:
                dado = (f'|G125|{linha[0]}|{linha[1]}|{linha[2]}|{linha[3]}|{linha[4]}|{linha[5]}'
                        f'|{linha[6]}|{linha[7]}|{linha[8]}|\n'
                        f'|G130|{linha[9]}|{linha[10]}|{linha[11]}|{linha[12]}|{linha[13]}|{linha[14]}|{linha[15]}||\n'
                        f'|G140|{linha[17]}|{linha[18]}|{linha[19]}|{linha[20]}|{linha[21]}||'
                        f'{linha[22]}|{linha[23]}|\n')
                file.write(dado)
            else:
                dado = (f'|G125|{linha[0]}|{linha[1]}|{linha[2]}|{linha[3]}|{linha[4]}|{linha[5]}'
                        f'|{linha[6]}|{linha[7]}|{linha[8]}|\n')
                file.write(dado)
                #excluir_ultima_linha_g()

    alterar_reg_g()

def gerar_300_305():
    consulta = 'SELECT * FROM reg_g'
    cursor.execute(consulta)
    with open('sped_reg_300_305.txt', 'w', encoding="utf8") as file:
        for linha in cursor.fetchall():
            dado_imobilizado = (f'|0300|{linha[0]}|{linha[9]}|{linha[27]}||1320201002|48|\n'
                    f'|0305|{linha[26]}|{linha[27]}|4|\n')
            file.write(dado_imobilizado)
    alterar_300_305()
    #excluir_ultima_linha_3()

def alterar_reg_g():
    search_text = "."
    replace_text = ","
    search_text2 = "?"
    replace_text2 = ""
    with open(r'sped_reg_g.txt', 'r') as file:
        data = file.read()
        data = data.replace(search_text, replace_text)
        data = data.replace(search_text2, replace_text2)
    with open(r'sped_reg_g.txt', 'w') as file:
        file.write(data)


def alterar_300_305():
    search_text3 = "."
    replace_text3 = ","
    search_text4 = "?"
    replace_text4 = ""
    with open(r'sped_reg_300_305.txt', 'r') as file:
        data = file.read()
        data = data.replace(search_text3, replace_text3)
        data = data.replace(search_text4, replace_text4)
    with open(r'sped_reg_300_305.txt', 'w') as file:
        file.write(data)

def excluir_ultima_linha_g():
    with open("sped_reg_g.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    with open("sped_reg_g.txt", "w") as arquivo:
        arquivo.writelines(linhas[:-1])

def excluir_ultima_linha_3():
    with open("sped_reg_300_305.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    with open("sped_reg_300_305.txt", "w") as arquivo:
        arquivo.writelines(linhas[:-1])



#excluir_ultima_linha_g()
#deleta_dados_antigos()
#sped_relatorio = Gerar_sped('reg_g.db')
#sped_relatorio.importa_relatorio()
#sped_relatorio.gerar_registro_g()
#sped_relatorio.gerar_300_305()
