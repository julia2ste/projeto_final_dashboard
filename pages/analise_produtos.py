import streamlit as st
import pandas as pd
import plotly.express as px
import locale 

# Função para formatar valores em reais
 
def format_brl(value):
    # Set the locale to Brazilian Portuguese
    # On some systems, the locale string might be slightly different (e.g., 'pt_BR.UTF-8')
    try:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    except locale.Error:
        # Fallback for systems where 'pt_BR.UTF-8' is not available
        try:
            locale.setlocale(locale.LC_ALL, 'pt_BR')
        except locale.Error:
            print("Warning: Could not set pt_BR locale. Falling back to simple formatting.")
            return f"R$ {value:,.2f}".replace('.', 'X').replace(',', '.').replace('X', ',')
 
    # Format the value as currency with grouping enabled
    # locale.currency() returns a string like 'R$ 1.234,56'
    formatted_value = locale.currency(value, symbol=True, grouping=True)
    return formatted_value

#criando uma variavel e colocar parta ler os dados de um arquivo
dados_produtos = pd.read_csv('dados/vendas.csv')

df = pd.DataFrame(dados_produtos)

#titulo da web
st.title(":rainbow[💼***Analise de produtos***]")

#Armazena na memoria do computador a opcao selecionada pelo usuario
option = st.selectbox(
     "**Escolha o produto:**",(['Headset','Mouse','Teclado','Headphone',
                                 'Wedcam','SSD','Memoria RAM'])
 )
#filtrando os dados de vendas usando a opcao selcionada pelo usuario
dados_filtrados = dados_produtos[ dados_produtos['Produto']  == option]

#st.table(dados_filtrados)

#Filtro de informacoes da metricas sobre receita, lucro, Qtd.Vendida, Preço meio
colA, colB,colC, colD = st.columns(4)
with colA:
    receita = dados_filtrados['Vendas'].sum()
    st.metric (label="Receita", value= format_brl(receita))

with colB:
    Lucro = dados_filtrados['Lucro'].sum()
    st.metric (label="Lucro", value= format_brl(Lucro))

with colC:
    qtd = dados_filtrados['Custo'].sum()
    st.metric (label="Qtd.Vendida", value= f'{qtd} unidades')

with colD:
    Preco_medio = receita / qtd
    st.metric (label="Preço medio", value= format_brl(Preco_medio))



col1,col2 = st.columns(2)
with col1:
     df_agrupado = dados_filtrados.groupby('Regiao')['Vendas'].sum().reset_index()
     fig =px.bar(df_agrupado, 
                 x='Regiao', 
                 y= 'Vendas', 
                 title= f'Headphone:Vendas por regiao - {option}')
     color_continuous_scale=px.colors.sequential.Sunset

     st.plotly_chart(fig, use_container_width=True)
# st.dataframe(df_agrupado)

with col2:
     dados_produtos.groupby('Vendedor')['Vendas'].sum().reset_index()
     fig = px.pie(dados_produtos, values='Vendas',
                      names='Vendedor',
                      title="Headphone: Vendas por Vendedor ")
     st.plotly_chart(fig, use_container_width=True)

#criando a coluna mes para analise temporal
#convertando a data em datetime
dados_filtrados ['Data'] =pd.to_datetime(dados_filtrados['Data'])

dados_filtrados['Mes'] = dados_filtrados['Data'].dt.to_period('M').astype(str)

#agrupar por mes
df_agrupado2 = dados_filtrados.groupby('Mes')['Vendas'].sum().reset_index()
#st.dataframe(dados_filtrados.head(10))
fig = px.area(df_agrupado2, x='Mes', y= 'Vendas', title= 'Evolucao Mensal de Teclado' )
#gerar o grafico
st.plotly_chart(fig, width='stretch')


