import streamlit as st
import pandas as pd
import plotly.express as px

def carregar_dados():
    #carregar os dados de vendas
    df = pd.read_csv('dados/vendas.csv')
    df['Data'] = pd.to_datetime(df['Data'])
    return df

#ultilizar a funcao para carregar os dados e armazenar em uma vasrialvekl para uso posterior

dados_vendas = carregar_dados

st.tatle(':moneybag: Analise  Detalhada de Vendas')

#filtros para analise
st.sidebar.header("Filtro De Vendas")
