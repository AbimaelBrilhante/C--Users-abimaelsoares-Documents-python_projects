def importa_sped():
    from tkinter import filedialog
    caminho_arquivo = filedialog.askopenfilename(initialdir="/home", title="Select a File",
                                                 filetypes=(("Text files", "*.*"), ("all files", "*.*")))
    print(caminho_arquivo)
    caminho_arquivo_provisorio.append(caminho_arquivo)

caminho_arquivo_provisorio = []
numero_da_linha = []
numero_da_linha_300 = []

def encontrar_linha_registro_sped_300():
    caminho_arquivo = caminho_arquivo_provisorio[0]
    registro_procurado_400 = "|0400|"

    with open(caminho_arquivo, "r") as arquivo:
        for num_linha_400, linha_400 in enumerate(arquivo, start=1):
            if registro_procurado_400 in linha_400:
                numero_da_linha_300.append(num_linha_400)
                print(num_linha_400)
                print(numero_da_linha_300)
                return num_linha_400
    print("Registro", registro_procurado_400, "não encontrado.")

def encontrar_linha_registro_sped():
    caminho_arquivo = caminho_arquivo_provisorio[0]
    registro_procurado = "|E990|"

    with open(caminho_arquivo, "r") as arquivo:
        for num_linha, linha in enumerate(arquivo, start=1):
            if registro_procurado in linha:
                numero_da_linha.append(num_linha)
                return num_linha
    print("Registro", registro_procurado, "não encontrado.")

def adicionar_frase_linha(texto, linha, frase):
    linhas = texto.split("\n")
    linhas.insert(linha - 1, frase)
    novo_texto = "\n".join(linhas)
    return novo_texto

def adicionar_frase_texto():
    caminho_arquivo = caminho_arquivo_provisorio[0]
    with open("sped_reg_g.txt", "r") as arquivo_origem:
        texto = arquivo_origem.read()

    linha_desejada = numero_da_linha[0]
    frase = texto

    with open(caminho_arquivo, "r") as arquivo:
        texto = arquivo.read()

    novo_texto = adicionar_frase_linha(texto, linha_desejada, frase)

    with open(caminho_arquivo, "w") as arquivo:
        arquivo.write(novo_texto)
        excluir_linhas_em_branco()

def adicionar_frase_texto_300():
    caminho_arquivo = caminho_arquivo_provisorio[0]
    with open("sped_reg_300_305.txt", "r") as arquivo_origem:
        texto = arquivo_origem.read()

    #linha_desejada = 24
    print(numero_da_linha_300)
    linha_desejada = numero_da_linha_300[0]
    frase = texto

    with open(caminho_arquivo, "r") as arquivo:
        texto = arquivo.read()

    novo_texto = adicionar_frase_linha(texto, linha_desejada, frase)

    with open(caminho_arquivo, "w") as arquivo:
        arquivo.write(novo_texto)
        excluir_linhas_em_branco()


def excluir_linhas_em_branco():
    caminho_arquivo = caminho_arquivo_provisorio[0]
    with open(caminho_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()

    linhas_sem_em_branco = [linha for linha in linhas if linha.strip()]

    with open(caminho_arquivo, "w") as arquivo:
        arquivo.writelines(linhas_sem_em_branco)


#adicionar_frase_linha('teste_adicionar_registro.txt',encontrar_linha_registro_sped(),"***************")


# importa_sped()
# encontrar_linha_registro_sped()
# adicionar_frase_texto()
# encontrar_linha_registro_sped_300()
# adicionar_frase_texto_300()

