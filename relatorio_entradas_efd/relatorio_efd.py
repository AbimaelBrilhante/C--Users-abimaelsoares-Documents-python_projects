import csv
import sqlite3


class Sped:
    def __init__(self, arquivo):
        self.conexao = sqlite3.connect(arquivo)
        self.cursor = self.conexao.cursor()

    def inserir(self, none_1, *args):
        consulta = 'INSERT OR IGNORE INTO sped_relatorio (none_1,REG_100,IND_OPER,IND_EMIT,COD_PART,COD_MOD,COD_SIT,' \
                   'SER,NUM_DOC,CHV_NFE,DT_DOC,DT_E_S,VL_DOC,IND_PGTO,VL_DESC_100,VL_ABAT_NT_100,VL_MERC,IND_FRT,' \
                   'VL_FRT,VL_SEG,VL_OUT_DA,VL_BC_ICMS_100,VL_ICMS_100,VL_BC_ICMS_ST_100,VL_ICMS_ST_100,VL_IPI_100,' \
                   'VL_PIS_100,VL_COFINS_100,VL_PIS_ST,VL_COFINS_ST,none_2,none_3,REG,NUM_ITEM,COD_ITEM,DESCR_COMPL,' \
                   'QTD,UNID,VL_ITEM,VL_DESC,IND_MOV,CST_ICMS,CFOP,COD_NAT,VL_BC_ICMS,ALIQ_ICMS,' \
                   'VL_ICMS,VL_BC_ICMS_ST,ALIQ_ST,VL_ICMS_ST,IND_APUR,CST_IPI,COD_ENQ,VL_BC_IPI,ALIQ_IPI,VL_IPI,' \
                   'CST_PIS,VL_BC_PIS,ALIQ_PIS_170,QUANT_BC_PIS,ALIQ_PIS,VL_PIS,CST_COFINS,VL_BC_COFINS,' \
                   'ALIQ_COFINS_170,QUANT_BC_COFINS,ALIQ_COFINS,VL_COFINS,COD_CTA,VL_ABAT_NT,none_4) VALUES(?,?,?,?,' \
                   '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,' \
                   '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
        self.cursor.execute(consulta, (none_1, *args))
        self.conexao.commit()

    def tratamento_arquivo(self):
        with open('SpedEFD-58128190002312-130782211-Remessa de arquivo original-abr2021.txt', 'r', encoding="utf8") as file:
            reader = csv.reader(file, delimiter='|')
            self.rows = list(reader)
            self.indicec100 = []
            self.indicec170 = []
            self.efd = []

            # FILTRAGEM DOS REGISTROS C100 (DE ENTRADA) E C170 DO ARQUIVO
            for efd_filt in self.rows:
                if (efd_filt[1] == "C100" and efd_filt[2] == "0" and efd_filt[3] == "1") or efd_filt[1] == "C170":
                    self.efd.append(efd_filt)

            # NUMERO DA LINHA QUE SE ENCONTRA O REGISTRO C100
            for indice, reg100 in enumerate(self.efd):
                if reg100[1] == "C100":
                    self.indicec100.append(indice)

            # NUMERO DA LINHA QUE SE ENCONTRA O REGISTRO C170
            for h, reg170 in enumerate(self.efd):
                if reg170[1] == "C170":
                    self.indicec170.append(h)

            # FAZENDO APPEND DO REGISTRO C100 E C170 PARA DENTRO DE UMA LISTA (PARA CADA C170 O C100 DEVERÁ SE REPETIR)
        x = 0
        y = 1
        self.contador = 0
        self.relatorio = []

        while (self.contador < len(self.indicec100) - 1):
            for r in range(self.indicec100[x] + 1, self.indicec100[y]):
                self.relatorio.append(self.efd[self.indicec100[x]] + self.efd[r])
            x += 1
            y += 1
            self.contador += 1

            # IDENTIFICANDO O ULTIMO C100 E SEUS CORRESPONDENTES (C170) E FAZENDO O APPEND NA MESMA LISTA DE CIMA

        quantidade_dos_ultimos_c170 = self.indicec170[-1] - self.indicec100[-1]
        k = 0
        while k < quantidade_dos_ultimos_c170:
            self.relatorio.append(
                self.efd[self.indicec100[len(self.indicec100) - 1]] + self.efd[self.indicec170[len(self.indicec170) - quantidade_dos_ultimos_c170 + k]])
            k += 1
        return self.relatorio

    # ADICIONANDO AS INFORMAÇÕES NO BANCO DE DADOS SQLITE
    def adicionar_bd(self):
        self.tratamento_arquivo()
        self.sped_relatorio = Sped('sped_relatorio.db')
        for r in self.relatorio:
            self.sped_relatorio.inserir(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13],
                                   r[14], r[15],r[16], r[17], r[18], r[19], r[20], r[21], r[22], r[23], r[24], r[25], r[26], r[27], r[28],
                                   r[29], r[30],r[31], r[32], r[33], r[34], r[35], r[36], r[37], r[38], r[39], r[40], r[41], r[42], r[43],
                                   r[44], r[45],r[46], r[47], r[48], r[49], r[50], r[51], r[52], r[53], r[54], r[55], r[56], r[57], r[58],
                                   r[59], r[60],r[61], r[62], r[63], r[64], r[65], r[66], r[67], r[68], r[69], r[70])

        for r in self.relatorio:
            print(r)

    def exportar_excel(self):
        pass


if __name__ == "__main__":

    Sped('sped_relatorio.db').adicionar_bd()





