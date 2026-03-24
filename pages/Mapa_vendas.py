import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

#criando uma variavel e colocar parta ler os dados de um arquivo
mapa_vendas = pd.read_csv('dados/vendas_geolocalizacao (1).csv')

df = pd.DataFrame(mapa_vendas)

st.title("🌍 Mapa de Vendas por Localização")
st.text('Visualize a distribuição geográfica das vendas e aplique filtros para explorar os dados')

#filtros para analise:
st.sidebar.header("Filtros Do Mapa")

#filtros por regiao
regioes = st.sidebar.selectbox(
         " regiao",
    options= mapa_vendas["Região"].unique(),
    index=0
)

#filtro por categorias
Categoria = st.sidebar.selectbox(
          "Categoria",
      options= mapa_vendas["Categoria"].unique(),
      index=0
  )
 #filtro por produtos
Produtos = st.sidebar.selectbox(
      "Produtos",
      options= mapa_vendas["Produto"].unique(),
      index=0
  )
#Filtro por vendedor
Vendedor = st.sidebar.selectbox(
        "Vendedor",
        options= mapa_vendas["Vendedor"].unique(),
        index=0
)

# recuperar as datas minimas e maximas do dataframe para configurar o filtro de data
mapa_vendas['Data'] = pd.to_datetime(mapa_vendas['Data'])

data_min = mapa_vendas['Data'].min().date()
data_max = mapa_vendas['Data'].max().date()   

 #filtro de periodo
periodo = st.sidebar.date_input(
     "Periodo",
     value=(data_min,data_max),
     min_value= data_min,
     max_value= data_max
 )
if len(periodo) == 2:
     data_inicio = pd.to_datetime(periodo[0])
     data_fim = pd.to_datetime(periodo[1])
else:
     st.warning("Por favor, selecione un intervalo de datas valido")
     st.stop()

#usando slider como filtro de valor por vendas
min_venda = df["Vendas"].min()
max_venda = df["Vendas"].max()

faixa = st.sidebar.slider(
    "Faixa de Valor da Venda (R$):",
    min_value=float(min_venda),
    max_value=float(max_venda),
    value=(float(min_venda), float(max_venda))
)

#aplicando os filtros selecionados pelo usuario para criar um dataframe filtrado
dados_filtrados = mapa_vendas[
(mapa_vendas["Região"]==regioes)&
(mapa_vendas["Categoria"]==Categoria)&
(mapa_vendas["Produto"]==Produtos) &
(mapa_vendas["Vendedor"]==Vendedor)&
(mapa_vendas["Data"].between(
       data_inicio,
       data_fim
     ))]




col1,col2,col3,col4 = st.columns(4)
with col1:
 st.metric("Pontos no Mapa", len(df))
with col2:
 st.metric("Cidades", df['Cidade'].nunique())
with col3:
 st.metric("Receita Filtrada", f"R$ {dados_filtrados['Vendas'].sum():,.0f}")
with col4:
 st.metric("Lucro Filtrado", f"R${dados_filtrados['Lucro'].sum():,.0f}")

st.text ("Distribuição Geográfica das Transações")
dados_filtrados.rename(columns={"Latitude":"LATITUDE","Longitude":"LONGITUDE"},inplace=True)

st.map(dados_filtrados)

#criando tabela sobre o resumo de imformacoes por cidades
st.title("Resumo por Cidade")

# resumo_dados = df.groupby(["Cidade", "Região"]).agg({
#     "Receita": "sum",
#     "Lucro": "sum",
# }).reset_index()

# resumo_dados=dados_filtrados[
#   (resumo_dados["Receita"]==(Vendas).sum())&
#   (resumo_dados['Cidade']==(Cidade))&
#   (resumo_dados['Região']== (regioes))&
#   (resumo_dados['Lucro']== (Lucro))
#   ]
 

st.dataframe( resumo_dados[['Cidade','Região','Lucro']].reset_index(drop=True))