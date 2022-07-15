import pandas as pd
planilha_mes = 'Apuração ICMS - ST29 06.2022.xlsb'
caminho = 'C:/Users/abimaelsoares/Desktop/CONCILIAÇÃO/'


df1 = pd.read_excel(f'{caminho}{planilha_mes}',sheet_name='F. Est. Crédito - Red. BC',skiprows = range(0, 9))
df2 = pd.read_excel(f'{caminho}{planilha_mes}', sheet_name='M. ICMS S.T Transferência',skiprows = range(0, 10))
df3 = pd.read_excel(f'{caminho}{planilha_mes}', sheet_name='O. ICMS ST Dev Interest',skiprows = range(0, 9))


concatenado = pd.concat([df1,df2,df3], axis=0)
df = pd.DataFrame(concatenado, columns = ["",'Material','Descrição','Un Med Básica','Segmento','CFOP','Qtd Un Med Básica','Vlr Total','Vlr Total',"",])
#df.sort_values(by=['Qtd Un Med Básica'],ascending=True, na_position='last').to_excel('final_output.xlsx', index=False)
df.to_excel('final_output.xlsx', index=False)
#print(df1.count())


