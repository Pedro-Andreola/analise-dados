from IPython.display import display
import pandas as pd
pd.set_option('display.max_columns', None)
tabela = pd.read_csv('./ClientesBanco.csv', encoding="latin1")
tabela = tabela.drop("CLIENTNUM", axis=1)
tabela = tabela.dropna()
display(tabela.describe().round(1))