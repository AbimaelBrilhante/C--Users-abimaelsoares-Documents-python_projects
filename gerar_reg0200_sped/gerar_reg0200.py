import sqlite3

class Gerar_sped:
    def __init__(self,arquivo):
        self.conexao = sqlite3.connect(arquivo)
        self.cursor = self.conexao.cursor()

    def gerar_registro_0200(self):
        consulta = 'SELECT * FROM reg_0200'
        self.cursor.execute(consulta)
        with open('sped_reg_0200.txt', 'w', encoding="utf8") as file:
            for linha in self.cursor.fetchall():
                dado = (f'|0200|{linha[0]}|{linha[1]}|{linha[2]}|{linha[3]}|{linha[4]}|{linha[5]}'
                      f'|{linha[6]}|{linha[7]}|{linha[8]}|{linha[9]}|{linha[10]}|{linha[11]}|\n')
                file.write(dado)




sped_relatorio = Gerar_sped('reg_0200.db')

sped_relatorio.gerar_registro_0200()
