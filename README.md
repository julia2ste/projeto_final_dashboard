# 📊 Dashboard de Análise de Vendas

> Um dashboard interativo e moderno para análise completa de dados de vendas com visualizações geográficas e métricas detalhadas.

<div align="center">

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

</div>

---

## 🎯 Sobre o Projeto

Este é um dashboard multipáginas desenvolvido para análise detalhada de dados de vendas. O projeto oferece visualizações intuitivas e interativas que permitem explorar métricas de vendas, análise de produtos, visão geográfica e muito mais com uma interface moderna e responsiva.

---

## ✨ Características Principais

- 📈 **Visão Geral** - Métricas consolidadas e KPIs principais
- 🛍️ **Análise de Produtos** - Desempenho e comparação de produtos
- 📍 **Mapa de Vendas** - Visualização geográfica das vendas
- 💰 **Análise de Vendas** - Detalhamento e tendências de vendas
- ℹ️ **Sobre** - Informações adicionais do projeto
- 🎨 **Interface Amigável** - Design moderno com paleta de cores aquecida
- 📱 **Layout Responsivo** - Funciona em diferentes tamanhos de tela

---

## 🛠️ Tecnologias Utilizadas

### Frontend & Framework
- **Streamlit** `1.55.0` - Framework web para aplicações de dados
- **Altair** `6.0.0` - Visualização declarativa em Python

### Data Science & Análise
- **Pandas** `2.3.3` - Manipulação e análise de dados
- **NumPy** `2.4.3` - Computação numérica
- **PyArrow** `23.0.1` - Processamento eficiente de dados

### Visualização
- **Plotly** `6.6.0` - Gráficos interativos
- **PyDeck** `0.9.1` - Visualização geográfica em mapas

### Utilitários
- **Pillow** `12.1.1` - Processamento de imagens
- **Requests** `2.32.5` - Requisições HTTP
- **Python-dateutil** `2.9.0` - Manipulação de datas

---

## 📸 Capturas de Tela

### Dashboard - Visão Geral
![Visão Geral do Dashboard](img/Captura%20de%20tela_24-3-2026_111223_localhost.jpeg)

### Dashboard - Análise Detalhada
![Análise de Vendas](img/Captura%20de%20tela_24-3-2026_111242_localhost.jpeg)

---

## 📁 Estrutura do Projeto

```
projeto_final_dashboard/
├── 📄 app.py                    # Arquivo principal da aplicação
├── 📄 gerar_dados.py            # Script para geração de dados
├── 📄 requirements.txt          # Dependências do projeto
├── 📄 README.md                 # Este arquivo
│
├── 📊 dados/                    # Pasta com dados
│   ├── vendas.csv              # Dados principais de vendas
│   └── vendas_geolocalizacao.csv # Dados com geolocalização
│
├── 🖼️ img/                      # Imagens do dashboard
│   ├── Captura de tela_24-3-2026_111223_localhost.jpeg
│   └── Captura de tela_24-3-2026_111242_localhost.jpeg
│
└── 📑 pages/                    # Páginas do dashboard
    ├── visao_geral.py          # Página inicial com métricas
    ├── analise_vendas.py       # Análise de vendas
    ├── analise_produtos.py     # Análise de produtos
    ├── Mapa_vendas.py          # Visualização geográfica
    └── sobre.py                # Página informativa
```

---

## 🚀 Como Instalar e Executar

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo 1: Clonar o Repositório
```bash
cd projeto_final_dashboard
```

### Passo 2: Criar Ambiente Virtual (Recomendado)
```bash
python -m venv venv

# No Windows
venv\Scripts\activate

# No Linux/Mac
source venv/bin/activate
```

### Passo 3: Instalar Dependências
```bash
pip install -r requirements.txt
```

### Passo 4: Gerar Dados (Se Necessário)
```bash
python gerar_dados.py
```

### Passo 5: Executar a Aplicação
```bash
streamlit run app.py
```

A aplicação se abrirá automaticamente no navegador em `http://localhost:8501`

---

## 📊 Páginas do Dashboard

| Página | Descrição | Ícone |
|--------|-----------|-------|
| **Visão Geral** | Métricas gerais e KPIs do período | 👀 |
| **Análise de Vendas** | Detalhamento e tendências de vendas | 📈 |
| **Análise de Produtos** | Desempenho de produtos | 🛍️ |
| **Mapa de Vendas** | Distribuição geográfica das vendas | 📍 |
| **Sobre** | Informações do projeto | ℹ️ |

---

## 🎨 Customização de Estilo

O projeto utiliza CSS customizado para uma paleta de cores moderna e aquecida:
- **Fundo Principal**: `#F5CE9D`
- **Barra Lateral**: `#ECB063`
- **Componentes**: `#F9D9B9`

Você pode customizar as cores editando o arquivo `app.py` na seção de estilos CSS.

---

## 📝 Arquivos de Dados

- **vendas.csv** - Dados brutos de vendas com todas as transações
- **vendas_geolocalizacao.csv** - Dados de vendas com coordenadas geográficas para visualização em mapas

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Submeter pull requests

---

## 📄 Licença

Este projeto está disponível sob a Licença MIT. Veja os detalhes para mais informações.

---

## 📧 Contato

Para dúvidas ou sugestões sobre o projeto, entre em contato através dos canais apropriados do repositório.

---

<div align="center">

**Feito com ❤️ para análise de dados**

![GitHub last commit](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=flat-square)

</div>
