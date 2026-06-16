import streamlit as st
import pandas as pd
import plotly.express as px
from google.cloud import storage
from PIL import Image
from io import BytesIO

# Dados de exemplo
df = pd.DataFrame({
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
    "Vendas": [120, 145, 98, 200, 175, 230],
    "Clientes": [40, 55, 35, 80, 70, 95],
})

st.dataframe(df, use_container_width = True)

# Cliente autenticado
client = storage.Client.from_service_account_info(
    st.secrets["gcp_service_account"]
)

bucket_nome = "bucket-copa"
arquivo = "imagens_jogadores/ale_1.jpg"

bucket = client.bucket(bucket_nome)
blob = bucket.blob(arquivo)

imagem_bytes = blob.download_as_bytes()

imagem = Image.open(BytesIO(imagem_bytes))

st.image(
    imagem,
    caption="Imagem do Datalake - Google Cloud Storage"
)
