import streamlit as st
#colorir o fundo 
st.markdown("""<style>
.stApp {
    background-color: #F5CE9D;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    """<style>
        [data-testid="stSidebar"] {
            background-color: #ECB063;
        }
    </style>
    """,
    unsafe_allow_html=True)

st.markdown("""
<style>
/* Targets the main selection area */
.stSelectbox div[data-baseweb="select"] > div:first-child {
    background-color: #F9D9B9; /* Light pink background */
    color: black; /* Text color */
}

/* Targets the dropdown list options */
div[role="listbox"] ul {
    background-color: #F9D9B9; /* Light pink background for list items */
}
</style>
""", unsafe_allow_html=True)
st.balloons()

#configuracao inicial de pagina
st.set_page_config(
    page_title="Dados de Vendas",
    page_icon=":bar_chart",
    layout="wide"
)

#Definindo as paginas
visao_geral = st.Page('./pages/visao_geral.py',
                     title= "Visao Geral",
                     icon='👀',
                     default=True
                   )


analise_vendas = st.Page('./pages/analise_vendas.py',
                        title='Analise de Vendas',
                        icon='🛒')

analise_produtos = st.Page('./pages/analise_produtos.py',
                          title='Produtos',
                          icon='📦')

sobre = st.Page('./pages/sobre.py',
                title='Sobre',
                icon='✅')

Mapa_vendas = st.Page('./pages/Mapa_vendas.py',
                      title='Mapa de Vendas',
                      icon='🗺️')
pg= st.navigation(
    [visao_geral,
     analise_vendas, 
     analise_produtos,
     sobre,
     Mapa_vendas]
) 

pg.run()