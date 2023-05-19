import xml.etree.ElementTree as ET
i=[]
def localizar_valor_xml(arquivo_xml, elemento_alvo):
    tree = ET.parse(arquivo_xml)
    root = tree.getroot()

    # Use o método findall para localizar todos os elementos com o nome desejado
    elementos_encontrados = root.findall(elemento_alvo)

    descricao_conta = []
    valor_conta=[]
    # Percorra os elementos encontrados e imprima os seus valores
    for elemento in elementos_encontrados:
        valor = elemento.text
        valor_conta.append(valor)
        descricao_conta.append(valor)
        try:
            indice = descricao_conta.index("Outras Receitas Operacionais")
            i.append(indice)

        except:
            pass

    print(valor_conta[i[0]])
# Exemplo de uso
localizar_valor_xml(r'C:\Users\abimaelsoares\Desktop\024228DFP28-02-2023v1.xml', 'DadosDFP/Formulario/DfIndividuais/DemonstracaoResultado/Conta/DescricaoConta')
localizar_valor_xml(r'C:\Users\abimaelsoares\Desktop\024228DFP28-02-2023v1.xml', 'DadosDFP/Formulario/DfIndividuais/DemonstracaoResultado/Conta/UltimoExercicio')
