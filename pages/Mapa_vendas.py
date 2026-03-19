import streamlit as st
import pandas as pd

#criando uma variavel e colocar parta ler os dados de um arquivo
mapas_vendas = pd.read_csv('dados/Vendas.csv')

st.title("🌍 Mapa de Vendas por Localização")
st.text('Visualize a distribuição geográfica das vendas e aplique filtros para explorar os dados')

# #filtrando os dados de vendas usando a opcao selcionada pelo usuario
# filtragem = Mapas_vendas[ Mapas_vendas['Regiao']  == option]
#filtros para analise

st.sidebar.header("Filtros Do Mapa")
regioes = st.sidebar.multiselect(
    "Regioes",
    options= mapas_vendas["Regiao"].unique(),
    default= mapas_vendas["Regiao"].unique()
)

Categoria = st.sidebar.multiselect(
    "Categoria",
    options= mapas_vendas["Categoria"].unique(),
    default= mapas_vendas["Categoria"].unique()
)
 
Produtos = st.sidebar.multiselect(
    "Produtos",
    options= mapas_vendas["Produtos"].unique(),
    default= mapas_vendas["Produtos"].unique()
)