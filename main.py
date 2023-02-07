import os
import pandas as pd
import plotly_express as px

lista_arquivo = os.listdir("C:\\Projetos\\Estudos TI\\Python\\Projeto\\Vendas\\bd_vendas_filiais")
tabela_total = pd.DataFrame()
for arquivo in lista_arquivo: 
    if "vendas" in arquivo.lower():
        tabela = pd.read_csv(f"C:\\Projetos\\Estudos TI\\Python\\Projeto\\Vendas\\bd_vendas_filiais\\{arquivo}")
        tabela_total = tabela_total.append(tabela)
print(tabela_total)

tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=True)
print(tabela_produtos)   

tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']

tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=True)
print(tabela_faturamento)

tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[["Faturamento"]]
print(tabela_lojas)


grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico.show()