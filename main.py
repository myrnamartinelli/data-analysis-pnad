#Análise econométrica da Educação em Rondônia.

#Importação dos dados da PNAD que estavam no STATA e das bibliotecas que serão utilizadas no projeto.
 
import pandas as pd
import numpy as np
reader = pd.read_stata('PNAD_painel_5_rs.dta',chunksize=10000)

df_PNAD_chunk = next(reader)

#print(df_PNAD_chunk.info())

'''Recorte dos dados: como a finalidade do projeto é analisar o estado de Rondônia, irei utilizar as informcações geográficas 
obtidas na PNAD para selecionar apenas os dados dessa região. '''

# utilizei o método isin para checar se a variável definida está contida na coluna 'UF' do dataframe
 
estados_RO = [11]
df_rondonia =  df_PNAD_chunk[df_PNAD_chunk['UF'].isin((estados_RO))]

print(df_rondonia)


'''Criação de dummy: nesta etapa faremos a coversão de variáveis qualitativas em variáveis numéricas, isso é necessário para 
implementar variáveis categóricas em análises de regressão. Foram separadas algumas variáveis consideradas importantes para
a análise que desejo fazer. '''


dummy_area_urb = pd.get_dummies(df_rondonia, columns=['V1022'])
dummy_chefe_de_domicilio = pd.get_dummies(df_rondonia, columns=["VD2002"])
dummy_sexo = pd.get_dummies(df_rondonia, columns=['V2007'])
dummy_raca = pd.get_dummies(df_rondonia, columns=['V2010'])
dummy_sabe_ler_escrever = pd.get_dummies(df_rondonia, columns=['V3001'])
dummy_freq_escola = pd.get_dummies(df_rondonia, columns=['V3002'])
dummy_rede_pub_priv = pd.get_dummies(df_rondonia, columns=['V3002A'])
dummy_anos_de_estudo = pd.get_dummies(df_rondonia, columns=['VD3006'])
dummy_nivel_de_instrucao = pd.get_dummies(df_rondonia, columns=['VD3004'])
dummy_num_pessoas_domicilio = pd.get_dummies(df_rondonia, columns=['V2001'])
dummy_rendimento_mensal = pd.get_dummies(df_rondonia, columns=['VD4020'])

print(dummy_area_urb)
print(dummy_chefe_de_domicilio)
print(dummy_sexo)
print(dummy_raca)
print(dummy_freq_escola)
print(dummy_rede_pub_priv)
print(dummy_anos_de_estudo)
print(dummy_nivel_de_instrucao)
print(dummy_num_pessoas_domicilio)
print(dummy_rendimento_mensal)

'''Nesta etapa realizarei uma análise descritiva dos dados acima, com intuito de melhor compreendê-los antes de aplicar técnicas
estatisticas mais avançadas '''

import matplotlib.pyplot as plt

"Area Urbana vs. Area Rural"




