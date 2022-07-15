import pandas as pd
import glob

path2 = r'X:\CONTROLADORIA\COMPLIANCE FISCAL\APURAÇÃO & CONCILIAÇÃO FISCAL\CONTROLES\Planilhas de Custo - Grupo 3Corações\2022\06 - Junho\Débito Posterior'
planilha1 = r'\Débito Posterior - ST29 06.2022.xlsm'
planilha2 = r'\Débito Posterior - ST30 06.2022.xlsm'

path = r'X:\CONTROLADORIA\COMPLIANCE FISCAL\APURAÇÃO & CONCILIAÇÃO FISCAL\CONTROLES\Planilhas de Custo - Grupo 3Corações\2022\06 - Junho\Débito Posterior'

filenames = glob.glob(path + "\*.xlsm")
print('File names:', filenames)

finalexcelsheet = pd.DataFrame()
arquivo_final=[]

'''finalexcelsheet = pd.DataFrame()

for file in filenames:
    df = pd.concat(pd.read_excel(
        file, sheet_name=None), ignore_index=True, sort=False)

    finalexcelsheet = pd.concat(
        df, ignore_index=True)'''

df = pd.concat(pd.read_excel(file) for file in filenames)
df.to_excel(r'Final.xlsx', index=False)

