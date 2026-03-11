import pandas as pd
import numpy as np

np.random.seed(42)
n = 2000
datas = pd.date_range('2023-01-01','2025-12-31', freq='D')

# gerar dados de vendas 
dados = pd.DataFrame({
    'Data': np.random.choice(datas, n),
    'Produto': np.random.choice('Headset','Mouse','Teclado','Headphone',
                                'Wedcam','SSD','Memoria RAM',n),
    'Categoria': np.random.choice(['Informatica'],n),
    'Regiao': np.random.choice(['Norte','Sul','Nordeste','Sudeste','Centro-Oeste'],n),
    'Vendedor': np.random.choice(['Ana Silva','Bruno Costa','Carla Dias','Doego Lima'],n),
    'Vendas': np.random.randint(150, 12000,n),
    'Quantidade': np.random.randint(1,30,n),
    'Custo':np.random.uniform(80,8000,n)
})