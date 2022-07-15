import pandas as pd
import glob


path = r'X:\CONTROLADORIA\COMPLIANCE FISCAL\APURAÇÃO & CONCILIAÇÃO FISCAL\CONTROLES\Planilhas de Custo - Grupo 3Corações\2022\06 - Junho\Débito Posterior'

filenames = glob.glob(path + "\*.xlsm")
print('File names:', filenames)

finalexcelsheet = pd.DataFrame()


for file in filenames:

    df = pd.concat(pd.read_excel(
        file, sheet_name=None), ignore_index=True, sort=False)


    finalexcelsheet = finalexcelsheet.append(
        df, ignore_index=True)

# to print the combined data
print('Final Sheet:')
print(finalexcelsheet)

finalexcelsheet.to_excel(r'Final.xlsx', index=False)