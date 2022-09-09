import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from pandas_datareader import data as pdr


#PEGANDO DADOS DA IBOVESPA

data_final = dt.datetime.now()
data_inicial = data_final - dt.timedelta(days=300)
ibovespa_precos = pdr.get_data_yahoo('''^BVSP''', data_inicial,data_final)['Adj Close']

#CALCULAR RETORNOS DIARIOS IBOV
retornos_ibov = ibovespa_precos.pct_change().dropna().to_numpy()

#PREMISSAS DA SIMULAÇÃO
num_dias = (3 * 252)
numero_simulacoes = 10000
dinheiro_inicial = 100000
lista_montante_final = np.array([])

#GUARDAR OS RESULTADOS DAS SIMULAÇÕES EMUMA LISTA
for n in range(numero_simulacoes):
    retorno_simulado = np.random.choice(retornos_ibov,
                                        size = num_dias, replace = True)
    resultado_acumulado = dinheiro_inicial * (retorno_simulado + 1).cumprod()
    montante_final = resultado_acumulado[-1]
    lista_montante_final = np.append(lista_montante_final,montante_final)

#ESTATISTICAS DAS SIMULAÇÕES
    montante_95 = "R$ "+str(np.percentile(lista_montante_final,95))
    montante_mediano = "R$ "+str(np.percentile(lista_montante_final,50))
    cenarios_com_lucro = str((len(lista_montante_final[lista_montante_final>1000])/len(lista_montante_final)) *100) + "%"

print(montante_95,montante_mediano,cenarios_com_lucro)


#CALCULAR O VAR
# R = RETORNO ESPERADO
# Z = VALOR CORRESPONDENTE PARA UM NIVEL DE SIGNIFICANCIA
# § = DESVIO PADRÃO DE RENTABILIDADE
# V = VALOR DO INVESTIMENTO

#VAR = | R - Z§ | V

# Considere que um ativo de R$ 100 milhões tem rentabilidade avaliada em 5% ao mês.
# O desvio padrão histórico do investimento é de 12% a.m.; além disso, o nível de significância é de 1,645%.
# Com um cálculo que tem 95% de confiança, temos o seguinte VaR:
# VaR = [5% – 1,645 x (12%)] x (100.000.000) = – R$ 14.740.
# Assim, o Value at Risk da operação é de R$ 14.740.  Ou seja, no período de 1 mês, a aplicação pode ter uma perda de R$ 14.740 em 95% dos dias operados. Em outros 5% do tempo, o prejuízo pode ser ainda maior. O mercado, dessa forma, fica ciente dos riscos potenciais da operação.


















# config = dict(histtype = "stepfilled",alpha = 0.8 ,density = False, bins = 150)
# fig, ax = plt.subplots()
# ax.hist(lista_montante_final,**config)
# ax.xaxis.set_major_formatter('R${X:.0f}')
# plt.title('Distribuição montantes finais com simulação MC')
# plt.xlabel('Montante final (R$)')
# plt.ylabel('Frequencia')
# plt.show()
