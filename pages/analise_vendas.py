import streamlit as st
import pandas as pd
import plotly.express as px

def carregar_dados():
    #carregar os dados de vendas
    df = pd.read_csv('dados/vendas.csv')
    df['Data'] = pd.to_datetime(df['Data'])
    return df

#ultilizar a funcao para carregar os dados e armazenar em uma variavel para uso posterior
dados_vendas = carregar_dados()

st.title(':moneybag: :yellow[Analise  Detalhada de Vendas]')

#filtros para analise
st.sidebar.header("Filtro De Vendas")

regioes = st.sidebar.multiselect(
    "Selecione as regioes",
    options=dados_vendas["Regiao"].unique(),
    default=dados_vendas["Regiao"].unique()
)


Categoria = st.sidebar.multiselect(
    "Selecione as Categorias",
    options=dados_vendas["Categoria"].unique(),
    default=dados_vendas["Categoria"].unique()
)

# recuperar as datas minimas e maximas do dataframe para configurar o filtro de data
data_min = dados_vendas["Data"].min().date()
data_max = dados_vendas["Data"].max().date()

#filtro de periodo
data_range = st.sidebar.date_input(
    "Selecione o periodo",
    value=(data_min,data_max),
    min_value=data_min,
    max_value=data_max
)
if len(data_range) == 2:
    data_inicio = pd.to_datetime(data_range[0])
    data_fim = pd.to_datetime(data_range[1])
else:
    st.warning("Por favor, selecione un intervalo de datas valido")
    st.stop()

#aplicando os filtros selecionados pelo usuario para criar um dataframe filtrado
dados_filtrados = dados_vendas[
    (dados_vendas["Regiao"].isin(regioes))&
    (dados_vendas['Categoria'].isin(Categoria))&
    (dados_vendas["Data"].between(
       data_inicio,
       data_fim
     ))
]

#metricas filtradas
col1, col2,col3 = st.columns(3)

col1.metric("Receita Filtrada", f"R$ {dados_filtrados['Vendas'].sum():,.0f}")
col2.metric("Lucro Filtrado", f"R${dados_filtrados['Lucro'].sum():,.0f}")


margem_media = 'N/A'
if dados_filtrados['Vendas'].sum() > 0:
    margem_media = (dados_filtrados['Lucro'].sum() / dados_filtrados['Vendas'].sum()*100)

    col3.metric("Margem Media", f"{margem_media}%")

st.subheader("***Performance por Vendedor***")

vendas_vendedor = dados_filtrados.groupby("Vendedor").agg(
    Receita=("Vendas","sum"),
    Lucro= ("Lucro","sum"),
    Transacoes=("Vendas","count"),
    Ticket_medio = ("Vendas","count")
).round(2).sort_values(by="Receita",ascending=False)

v_col1, v_col2 = st.columns(2)

with v_col1:
    st.text("💼Tabela de dados por vendedor ")
    st.dataframe(vendas_vendedor,width='stretch', height=300)

with v_col2:
    fig =px.bar(
        vendas_vendedor.reset_index(),
        x='Vendedor',
        y= "Receita",
        title="Receita e Lucro por vendendor",
        color="Lucro",
        color_continuous_scale=px.colors.sequential.Sunset,
    )
    st.plotly_chart(fig, width='stretch')

    #analise temporal de vendas
st.subheader("📊***Analise Temporal***")


dados_filtrados['Mes']= dados_filtrados['Data'].dt.strftime('%m/%Y')
mensal= dados_filtrados.groupby('Mes').agg(
    Receita =('Vendas','sum'),
    Lucro = ('Lucro', 'sum')
).reset_index()


fig = px.bar(
    mensal, x='Mes', y= ['Receita','Lucro'],
    barmode='group', title='Receita x Lucro Mensal')
    
fig.update_layout(xaxis_tickangle=45)

#exibe o grafico usando streamlit com a largura configurada
#para se estender ao maximo do conteiner disponivel
st.plotly_chart(fig, width='stretch')

#tabela de dados
# realiza o dowload dos dados filtrados em formato csv, permitindo que os usuarios baixem os dados
with st.expander("Dados Detalhados"):
    st.dataframe(dados_filtrados,width='stretch')
    CSV = dados_filtrados.to_csv(index=False).encode('utf-8')
    st.download_button('Baixar dados filtrados', data=CSV, file_name='dados_filtrados.csv',mime='text/csv')