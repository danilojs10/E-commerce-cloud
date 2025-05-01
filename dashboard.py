import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Exemplo de dados de vendas de um e-commerce
data = {
    "Produto": ["Produto A", "Produto B", "Produto C", "Produto D", "Produto E"],
    "Categoria": ["Categoria 1", "Categoria 2", "Categoria 1", "Categoria 3", "Categoria 2"],
    "Vendas": [150, 200, 120, 90, 300],
    "Receita": [1500, 2500, 1200, 900, 3000]
}

# Criando um DataFrame
df = pd.DataFrame(data)

# Iniciando o aplicativo Dash
app = dash.Dash(__name__)

# Layout do dashboard
app.layout = html.Div([
    html.H1("Dashboard de E-commerce", style={"textAlign": "center"}),

    # Total de vendas
    html.Div([
        html.H3(f"Total de Vendas: {df['Vendas'].sum()}"),
        html.H3(f"Receita Total: R${df['Receita'].sum()}"),
    ], style={"textAlign": "center"}),

    # Gráfico de vendas por produto
    html.Div([
        dcc.Graph(
            id='vendas-produtos',
            figure=px.bar(df, x='Produto', y='Vendas', title='Vendas por Produto')
        ),
    ], style={"padding": "20px"}),

    # Gráfico de receita por categoria
    html.Div([
        dcc.Graph(
            id='receita-categoria',
            figure=px.pie(df, names='Categoria', values='Receita', title='Receita por Categoria')
        ),
    ], style={"padding": "20px"}),
])

# Rodando o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
