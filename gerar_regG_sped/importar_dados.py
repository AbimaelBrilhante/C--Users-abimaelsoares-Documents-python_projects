import sqlite3
from tkinter import filedialog
import pandas as pd

conexao = sqlite3.connect('ciap.db')
cursor = conexao.cursor()

def importa_relatorio_ciap():
    filename_saida = filedialog.askopenfilename(initialdir="/home", title="Select a File",
                                                    filetypes=(("Text files", "*.*"), ("all files", "*.*")))
    wb1 = pd.read_excel(filename_saida, sheet_name='Exportação SAPUI5')
    wb1.to_sql(name='ciap_s4hana', con=conexao, if_exists='append', index=False)

def importa_relatorio_zsdr133():
    filename_saida = filedialog.askopenfilename(initialdir="/home", title="Select a File",
                                                    filetypes=(("Text files", "*.*"), ("all files", "*.*")))
    wb1 = pd.read_excel(filename_saida, sheet_name='Exportação SAPUI5')
    wb1.to_sql(name='entradas_fiscais', con=conexao, if_exists='append', index=False)

def importa_tabela_anek():
    filename_saida = filedialog.askopenfilename(initialdir="/home", title="Select a File",
                                                    filetypes=(("Text files", "*.*"), ("all files", "*.*")))
    wb1 = pd.read_excel(filename_saida, sheet_name='Sheet1')
    wb1.to_sql(name='anek', con=conexao, if_exists='append', index=False)

def criar_relatorio_ciap_consolidado():
    cursor.execute("""CREATE TABLE CIAP_CONSOLIDADO AS SELECT "Nota Fiscal"	AS NF,	"Nº Documento"	AS	DOCNUM,	entradas_fiscais."Empresa"	AS	EMPRESA,	"Local de negócio"	AS	LOC_NEG,	"Parceiro"	AS	COD_PART,	
"Nº CNPJ"	AS	CNPJ_PART,	"Nº CPF"	AS	CPF_PART,	entradas_fiscais."Data de lançamento"	AS	DATA_LANCAMENTO,	"Item NF"	AS	NUM_ITEM,	
entradas_fiscais."Material"	AS	MATERIAL,	"Texto breve material"	AS	DESCRICAO_MATERIAL,	"NCM"	AS	NCM,	"CFOP"	AS	CFOP,	
"Qdt. Un. Med. Básica"	AS	QTD,	"Un. Med. Básica"	AS	UND_MEDIDA,	"Valor Total"	AS	VLR_TOTAL,	"Valor Produtos"	AS	VLR_PRODUTOS,	
"Valor ICMS"	AS	VLR_ICMS,	"IVA"	AS	IVA,	"Item Pedido de Compra"	AS	ITEM_PEDIDO,	"Pedido de Compra"	AS	PEDIDO,
"Doc. MIRO"	AS	DOC_MIRO,	"Doc.referência"	AS	DOC_REF,	"Conta Contábil Pedido"	AS	CC_PEDIDO,	"Descrição da Conta"	AS	DESCRICAO_CC,	
"Chave de Acesso"	AS	CHV_NFE_CTE,	"Dt.iníc.depreciação"	AS	DT_INICIO_DEPRECIACAO,	"Tp.movimento imob."	AS	TP_MOVIMENTO,	
"Subnº"	AS	SUB_ITEM,	ciap_s4hana."Imobilizado"	AS	IMOBILIZADO,	"Nº do imobilizado"	AS	"IMOBILIZADO+SUBITEM",	"Centro custo ativo"	AS	CENTRO_CUSTO,	
"Classe imobilizado"	AS	CLASSE,	"Determ.contas"	AS	DETERM_CONTAS,	"Vida útil planejada"	AS	VIDA_UTIL_PLANEJADA,	
"Transação CAP"	AS	TRANS_CAP,	"Ajuste do valor"	AS	AJ_VALOR,	"Ano de aquisição"	AS	ANO_AQUISICAO,	ciap_s4hana."Atribuição"	AS	ATRIBUICAO,	
"Baixa"	AS	BAIXA,	"Chave de depreciação"	AS	CHV_DEPRECIACAO,	"Ctg.tipo movimento"	AS	CTG_TIPO_MOV,	"Data da criação"	AS	DT_CRIACAO,	
"Data de referência"	AS	DT_REFERENCIA,	"Depreciação baixa"	AS	DEPRECIACAO_BAIXA,	"Dt.lnçmto.cont."	AS	DT_LANÇAMENTO_CONTABIL,
"Elemento PEP"	AS	ELEMENTO_PEP,	ANEK."Referência"	AS	REFERENCIA,	ciap_s4hana."Período contábil"	AS	PERIODO_CONTABIL,	"Mont.moeda empresa"	AS	MONTANTE,	
"Depreciação normal"	AS	DEPRECIACAO_NORMAL

FROM entradas_fiscais
INNER JOIN ANEK ON entradas_fiscais."Doc. MIRO" = ANEK."Doc.ref."
	   AND entradas_fiscais."Pedido de Compra" = ANEK."Doc.compra" 
	   AND entradas_fiscais."Item Pedido de Compra" = ANEK."Item"
	  
INNER JOIN ciap_s4hana ON ANEK."Doc.ref." = ciap_s4hana."Doc.referência"
	   AND ANEK."Imobilizado" = ciap_s4hana."Imobilizado"
	   AND entradas_fiscais."Doc. MIRO" = ciap_s4hana."Doc.referência"
WHERE ANEK."Op.refer." = "RMRP" and ciap_s4hana."Está estornando" = 0 """)

def gerar_relatorio_ciap_consolidado():
    df = pd.read_sql("select * from CIAP_CONSOLIDADO", conexao)
    df.to_excel(r"C:\TEMP\CIAP_CONSOLIDADO.xlsx", index=False)

if __name__ == "__main__":
    # importa_relatorio_ciap()
    # importa_relatorio_zsdr133()
    # importa_tabela_anek()
    # criar_relatorio_ciap_consolidado()
    # gerar_relatorio_ciap_consolidado()
    pass



#ADICIONAR EMPRESA NA VALIDAÇÃO DO INNER JOIN DO IMOBILIZADO

