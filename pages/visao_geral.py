import streamlit as st
import pandas as pd
import plotly.express as px


def carregar_dados():
# carregar os daods de vendas
    df = pd.read_csv('dados/vendas.csv')
    return df

#utilizar a funcao para carregar os dados
# e armazenar em uma variavel para o posterior
# e um dataframe do pandas que contem os dados de vendas
dados_vendas = carregar_dados()

st.title("***:red[Visao] :orange[Geral de] :yellow[Negocio] :green[𓁹‿𓁹]***")

#KPIs principais
col1, col2 ,col3 ,col4 =st.columns(4)

#coluna 1 exibe a receita total, formatada como moeda brasdileira
col1.metric(":moneybag: Receita Total", f"R${dados_vendas['Vendas'].sum():,.2f}")

#coluna 2 exibe o lucro total, formatado com moeda bresileira
col2.metric(":chart_with_upwards_trend: Lucro Total", f"R${dados_vendas['Lucro'].sum():,.2f}")

#coluna 3 exibe o total de transacoes , que e o numero de linhas no dataframe de vendas
col3.metric(":shopping_cart: Total Transacoes", f"{len(dados_vendas)}")

#coluna 4             
col4.metric(":bar_chart: Ticket Medico", f"R${dados_vendas['Vendas'].mean():,.2f}")

st.divider()


colA, colB = st.columns(2)

with colA:
    #agrupando os daods por regiao e somar as vendas
    vendas_regioes = dados_vendas.groupby('Regiao')['Vendas'].sum().reset_index()


#criando um grafico de pizza para mostrar a distribuicao de vendas por regiao
    fig = px.pie(vendas_regioes, names= 'Regiao', values='Vendas',
                 title= 'Distribuicao De Vendas Por Regiao',
                hole=0.4)
    

#exibir o grafico usando streamlit
    st.plotly_chart(fig,width='stretch')

with colB:
    dados_vendas['Data'] = pd.to_datetime(dados_vendas['Data'])
    dados_vendas['Mes'] = dados_vendas['Data'].dt.to_period('M').astype(str)

# Agrupando os dados por mes e somar as vendas 
    vendas_mensal = dados_vendas.groupby('Mes')['Vendas'].sum().reset_index()

#criando um grafico de linha para mostrar a evolucao mensal das vendas
    fig = px.line(vendas_mensal, x= 'Mes', y='Vendas',
                 title='Evolucao Mensal de Vendas',
                 markers= True) 

#exibindo o grafico usando streamlit
    st.plotly_chart(fig,width='stretch')

#tpo 5 produtos
    st.subheader(":moneybag: Tpo 5 Produtos Por Receita")

#agrupando os dados por podrutio e somar as vendas
#depois selecionar os 5 produtos com maior receita
    top5_produtos = dados_vendas.groupby('Produto')['Vendas'].sum().nlargest(5).reset_index()

#criando um grafico de basrras para mostrar os top 5 produtios por receita, com as barras coloridas 
#de acordo com o valor das vendas   
    fig = px.bar(top5_produtos, x='Produto', y='Vendas',
                 title='Top 5 Produtos',
                 color='Vendas',
                 color_continuous_scale='gnbu')
    
    st.plotly_chart(fig, width='stretch')


