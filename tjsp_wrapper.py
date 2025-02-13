import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri

class TJSPWrapper:
    def __init__(self):
        pandas2ri.activate()  # Ativa conversão R <-> pandas
        self.tjsp = importr("tjsp")
        self.auth = False
        print(self.tjsp.__repr__())

    def autenticar(self, usuario: str, senha: str) -> bool:
        """Autentica no TJSP usando credenciais."""
        auth_func = robjects.r("tjsp_autenticar")
        self.auth = auth_func(usuario, senha)[0]  # Converte para booleano
        return self.auth

    def baixar_cpopg(self, processo: str, diretorio: str = "data") -> str:
        """Baixa dados de um processo."""
        if not self.auth:
            raise PermissionError("Autentique-se primeiro.")
        baixar_func = robjects.r("baixar_cpopg")
        resultado = baixar_func(processo, diretorio)
        return str(resultado)

    def ler_dados(self, diretorio: str):
        """Lê dados baixados e retorna um DataFrame pandas."""
        ler_func = robjects.r("ler_cpopg")
        df_r = ler_func(diretorio)
        return pandas2ri.rpy2py(df_r)  # Converte para pandas DataFrame
    
    def baixar_cjsg(self, livre: str, diretorio: str):
        """Baixa dados do banco de sentença 

            *params:
            livre: tema para buscar livre
        """
        baixar_func = robjects.r("tjsp_baixar_cjsg")
        resultado = baixar_func(livre, diretorio)
        return resultado