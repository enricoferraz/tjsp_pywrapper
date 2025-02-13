import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri

pandas2ri.activate()  # Ativa conversão R <-> pandas
utils = importr("utils")
dplyr = importr("dplyr")
#tjsp = importr("tjsp")

robjects.r('data(iris)')

robjects.r('''
    library(dplyr)
    iris_summary <- iris %>%
    group_by(Species) %>%
    summarise(
           Avg_Sepal.Length = mean(Sepal.Length),
           Avg_Sepal.Width = mean(Sepal.Width))
           ''')


iris_summary = pandas2ri.rpy2py(robjects.r['iris_summary'])
print(iris_summary)

# from tjsp_wrapper import TJSPWrapper
# import os

# print(os.environ.get("R_HOME"))  # Deve retornar o caminho correto
# # Teste de autenticação e download
# wrapper = TJSPWrapper()
# #wrapper.autenticar("meu_usuario", "minha_senha")
# #wrapper.baixar_cpopg("1234567-89.2020.8.26.0000", "dados_tjsp")

# result = wrapper.baixar_cjsg(livre='feminicidio', diretorio='feminicidio')
# print(result)

# # Teste de leitura de dados
# df = wrapper.ler_dados("dados_tjsp")
# print(df.head())

# print(os.environ.get("R_HOME"))  # Deve retornar o caminho correto