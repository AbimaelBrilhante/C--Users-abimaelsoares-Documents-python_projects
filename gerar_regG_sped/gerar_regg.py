import sqlite3

class Gerar_sped:
    def __init__(self,arquivo):
        self.conexao = sqlite3.connect(arquivo)
        self.cursor = self.conexao.cursor()

    def gerar_registro_0200(self):
        consulta = 'SELECT * FROM reg_g'
        self.cursor.execute(consulta)
        with open('sped_reg_g.txt', 'w', encoding="utf8") as file:
            for linha in self.cursor.fetchall():
                dado = (f'|G125|{linha[0]}|{linha[1]}|{linha[2]}|{linha[3]}|{linha[4]}|{linha[5]}'
                      f'|{linha[6]}|{linha[7]}|{linha[8]}|\n'
                        f'|G130|{linha[8]}|{linha[9]}|{linha[10]}|{linha[11]}|{linha[12]}|{linha[13]}|{linha[14]}|{linha[15]}|\n'
                        f'|G140|{linha[16]}|{linha[17]}|{linha[18]}|{linha[19]}|{linha[20]}|{linha[21]}|'
                        f'{linha[22]}|{linha[23]}|\n')
                file.write(dado)
                print(dado)




sped_relatorio = Gerar_sped('reg_g.db')

sped_relatorio.gerar_registro_0200()
