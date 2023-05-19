import xml.etree.ElementTree as ET

def localizar_valor_xml(arquivo_xml, elemento_alvo):
    tree = ET.parse(arquivo_xml)
    root = tree.getroot()

    # Use o método findall para localizar todos os elementos com o nome desejado
    elementos_encontrados = root.findall(elemento_alvo)

    lista=[]
    # Percorra os elementos encontrados e imprima os seus valores
    for elemento in elementos_encontrados:
        valor = elemento.text
        lista.append(elemento)

        tag_encontrada = root.find("Receita de Venda de Bens e/ou Serviços")
        conteudo_tag = tag_encontrada.text if tag_encontrada is not None else None
        print(conteudo_tag)
        print((elemento.findall("DescricaoConta")))
        print(elemento.findall("UltimoExercicio"))

# Exemplo de uso
localizar_valor_xml(r'C:\Users\abimaelsoares\Desktop\024228DFP28-02-2023v1.xml', 'DadosDFP/Formulario/DfIndividuais/DemonstracaoResultado/Conta')
