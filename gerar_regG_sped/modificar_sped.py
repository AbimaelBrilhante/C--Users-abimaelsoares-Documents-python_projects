numero_da_linha = []
def encontrar_linha_registro_sped():
    caminho_arquivo = "teste_adicionar_registro.txt"  # Substitua pelo caminho do arquivo SPED
    registro_procurado = "|E990|"

    with open(caminho_arquivo, "r") as arquivo:
        for num_linha, linha in enumerate(arquivo, start=1):
            if registro_procurado in linha:
                print(num_linha)
                numero_da_linha.append(num_linha)
                print(numero_da_linha)
                return num_linha
    print("Registro", registro_procurado, "não encontrado.")


def adicionar_frase_linha(texto, linha, frase):
    linhas = texto.split("\n")
    linhas.insert(linha - 1, frase)
    novo_texto = "\n".join(linhas)
    return novo_texto

def adicionar_frase_texto():
    caminho_arquivo = "teste_adicionar_registro.txt"  # Substitua pelo caminho do arquivo de texto
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


def excluir_linhas_em_branco():
    with open("teste_adicionar_registro.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    linhas_sem_em_branco = [linha for linha in linhas if linha.strip()]

    with open("teste_adicionar_registro.txt", "w") as arquivo:
        arquivo.writelines(linhas_sem_em_branco)


#encontrar_linha_registro_sped()
adicionar_frase_linha('teste_adicionar_registro.txt',encontrar_linha_registro_sped(),"***************")
adicionar_frase_texto()
#adicionar_frase_arquivo()