import streamlit as st

#configuracao inicial de pagina
st.set_page_config(
    page_title="Dados de Vendas",
    page_icon=":bar_chart",
    layout="wide"
)

#Definindo as paginas
visao_geral = st.Page('./pages/visao_geral.py',
                     title= "Visao Geral",
                     icon='✈',
                     default=True
                   )

#analise_vendas = st.Page('./pages/analise_vendas.py',
 #                        title='Analise de Vendas',
 #                        icon=':moneybag:'
#                       )

#analise_produtos = st.page('/pagesa/analise_produtos.py',
 #                         title= 'Produtos',
  #                        icon=':package:'
   #                       )

#sobre = st.page('./pages/sobre.py',
 #               title='Sobre',
  #              icon=':information_source:'
   #             )

pg= st.navigation(
    [
        visao_geral
    ]
) 

pg.run()