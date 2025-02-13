import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri

# Ativar a conversão automática entre pandas DataFrame e R DataFrame
pandas2ri.activate()

# Importar o pacote tjsp
tjsp = importr('tjsp')

print(tjsp._exported_names)

# Definir a função R que será utilizada
baixar_cjpg = robjects.r['tjsp_baixar_cjsg']

# Chamar a função com os parâmetros desejados
#baixar_cjpg('pesquisa', 'data_inicial', 'data_final', 'diretorio')

# Supondo que a função R retorne um DataFrame
baixar_cjpg('feminicidio', 'feminicidio')


# # Agora 'df' é um DataFrame do pandas e pode ser manipulado no Python
# print(df.head())

