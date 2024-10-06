# Importar Bibliotecas
from IPython.display import display
import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "vscode"

# Configuração do Display
pd.set_option('display.max_columns', None)

# Importar base de dados
tabela = pd.read_csv('./ClientesBanco.csv', encoding="latin1")

# Remover a coluna ClienteNum
tabela = tabela.drop("CLIENTNUM", axis=1)

# Remover linhas que tenham um valor vazio
tabela = tabela.dropna()

# Exibe o numero de Clientes x Cancelamentos
qtde_categoria = tabela["Categoria"].value_counts()
display(qtde_categoria)

# Exibe a porcentagem de Clientes x Cancelamentos
qtde_categoria_perc = tabela["Categoria"].value_counts(normalize=True)
display(qtde_categoria_perc)

# Grafico
grafico = px.histogram(tabela, x="Idade", color="Categoria")