import csv

with open("63310411003038 - cat42 - 2020-04-01 - MA.txt",'r',encoding="utf8") as file:
    reader = csv.reader(file, delimiter='|')
    rows = list(reader)

    reg_1050 = []
    for seq, campo in enumerate(rows):
        if campo[0] == '1050':
            reg_1050.append(seq)
            tamanho = len(reg_1050)

    qtd_materiais=int(reg_1050[0])

    total = 0
    for i in rows:
        if i[0] == "1100" and int(i[10].replace("", "0")) > 0:
            total += float(i[9].replace(",", "."))

    while qtd_materiais <(int(reg_1050[0])+tamanho):
        material = rows[qtd_materiais][1]

        for y,i in enumerate(rows):
            if i[0]=='1050' and i[1]==material:
                inicial = float(i[2].replace(',','.'))

        for n,f in enumerate(rows) :
            if f[0] and f[5]==material and f[6][:1]=='5':
                inicial-=float(f[7].replace(',','.'))
                if inicial<0:
                    print(f'quantidade negativa - linha: {n+1} e material: {material} e data: {f[2]}')
            elif f[0] and f[5] == material and f[6][:1] == '6':
                inicial -= float(f[7].replace(',', '.'))
                if inicial<0:
                    print(f'quantidade negativa - linha: {n+1} e material: {material} e data: {f[2]}')
            elif f[0] and f[5]== material and f[6][:1]=='1':
                inicial+=float(f[7].replace(',','.'))
            elif f[0] and f[5]==material and f[6][:1]=='2':
                inicial+=float(f[7].replace(',','.'))


            else:
                pass
        qtd_materiais+=1
    print('Total a ressarcir: {:.2f}'.format((float(total))))

    print('Validação finalizada')
##########################################################################

"""file_old = open("63310411003038 - cat42 - 2019-12-01 - MA.txt",'r',encoding="utf8")
file_new = open("arquivo_cat_novo.txt",'w+',encoding="utf8")


for line in file_old:
    if line[:4]=="1100" and line[-6:] == "0,00|1" :
        file_new.write(line[:-6]+ "|0,01|1")
    elif line[:4] == "1100" and line[-6:] == "0,00|2":
        file_new.write(line[:-6]+ "|0,01|2")
    elif line[:4] == "1100" and line[-6:] == "0,00|3":
        file_new.write(line[:-6]+ "|0,01|3")
    elif line[:4] == "1100" and line[-6:] == "0,00|4":
        file_new.write(line[:-6]+ "|0,01|4")
    else:
        file_new.write(line)

file_old.close()
file_new.close()"""



