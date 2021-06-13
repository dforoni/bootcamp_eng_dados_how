# Coletar os dados do site da Caixa Economica Federal

# a proposta coletar os dados da lotofacil e realizar analises com eles
# 1. Qual o numero mais sorteado e o menos sorteado?
# 2. Quais combinacoes de numeros Pares, Impares e Primos que saem por sorteio?

# biblioteca necessaria

import requests
import pandas as pd

# link Caixa Economica Federal
url = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotofacil/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbz8vTxNDRy9_Y2NQ13CDA0sTIEKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wBmoxN_FydLAGAgNTKEK8DkRrACPGwpyQyMMMj0VAcySpRM!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0K85260Q5OIRSC42046/res/id=historicoHTML/c=cacheLevelPage/=/'

# fazendo o requerimento dos dados
r = requests.get(url)
# para saber o valor
r_text = r.text

# # criando um dataframe
df = pd.read_html(r_text)

# # verificando o tipo da variavel df
print(type(df))

# #verificando o tipo da variavel df na primeira posicao
type(df[0])

# criando um novo dataframe apenas com as informacoes dos dados dos jogos
df = df[0].copy()


# criando a populacao dos jogos, que sera 15 numeros de 25 
nr_pop = list(range(1,26))


