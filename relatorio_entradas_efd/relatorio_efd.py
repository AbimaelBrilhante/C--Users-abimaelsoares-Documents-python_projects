import csv
import sqlite3

class Sped:
    def __init__(self,arquivo):
        self.conexao = sqlite3.connect(arquivo)
        self.cursor = self.conexao.cursor()

    def inserir(self, none_1,*args):

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
        self.cursor.execute(consulta,(none_1,*args))
        self.conexao.commit()


with open('sped_modelo.txt', 'r',encoding="utf8") as file:
    reader = csv.reader(file, delimiter='|')
    rows = list(reader)
    i = []
    efd_quantidade = []
    efd_filtrada=[]
    efd = []



    for efd_filt in rows:
        if (efd_filt[1] == "C100" and efd_filt[2] == "0" and efd_filt[3] == "1") or efd_filt[1] == "C170":
            efd.append(efd_filt)
    for indice, reg100 in enumerate(efd):
        if reg100[1]== "C100":
            i.append(indice)

for j,e in enumerate(efd):
    i.append(j)

arquivo_para_bd = []
x = 0
y = 1
contador = 0
relatorio = []
while (contador < len(i)-1):
    for r in range(i[x]+1, i[y]):
        relatorio.append(efd[i[x]]+efd[r])
        arquivo_para_bd.append(efd[i[x]])
    x += 1
    y += 1
    contador += 1


sped_relatorio = Sped('sped_relatorio.db')

for r in relatorio:
    sped_relatorio.inserir(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12],r[13],r[14],r[15],
                           r[16],r[17],r[18],r[19],r[20],r[21],r[22],r[23],r[24],r[25],r[26],r[27],r[28],r[29],r[30],
                           r[31],r[32],r[33],r[34],r[35],r[36],r[37],r[38],r[39],r[40],r[41],r[42],r[43],r[44],r[45],
                           r[46],r[47],r[48],r[49],r[50],r[51],r[52],r[53],r[54],r[55],r[56],r[57],r[58],r[59],r[60],
                           r[61],r[62],r[63],r[64],r[65],r[66],r[67],r[68],r[69],r[70])
#print(r)










