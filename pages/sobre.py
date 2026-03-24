import streamlit as st
import pandas as pd

#criando uma variavel e colocar parta ler os dados de um arquivo
sobre = pd.read_csv('dados/vendas.csv')

st.title("❗Sobre a web")

st.text('Vendas são uma parte essencial de qualquer negócio,' \
' pois representam o momento em que um produto ou serviço realmente gera valor. Mais do que simplesmente ' \
'oferecer algo, vender envolve entender as necessidades do cliente,' \
' criar conexão e apresentar soluções que façam sentido para ele.')

st.header("Pontos principais sobre vendas:")

st.text('***Os pontos essenciais sobre vendas sao baseados em:***')
st.text('-Entender a necessidade do cliente')
st.text('-Ter boa comunicação')
st.text('-Conhecer bem o produto ou serviço')
st.text('-Criar confiança com o cliente')
st.text('-Oferecer soluções, não apenas produtos')
st.text('-Ter bom atendimento')
st.text('-Saber ouvir mais do que falar')
st.text('-Usar estratégias de marketing')
st.text('-Aproveitar ferramentas digitais e redes sociais')
st.text('-Buscar fidelizar o cliente')

st.image('https://media1.tenor.com/m/2f31yo7eV6kAAAAC/confused-confusion.gif')