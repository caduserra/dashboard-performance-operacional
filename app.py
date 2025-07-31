import streamlit as st
import pandas as pd
import plotly.express as px

# Simulando base de dados
data = {
    "Operador": ["Ana", "Bruno", "Carlos", "Ana", "Bruno", "Carlos"],
    "Mês": ["Jan", "Jan", "Jan", "Fev", "Fev", "Fev"],
    "Vendas": [10, 15, 12, 14, 18, 16],
    "TMA": [300, 320, 310, 290, 315, 300],
    "Qualidade": [92, 88, 90, 93, 89, 91],
    "Pausa": [40, 60, 50, 35, 55, 45]
}

df = pd.DataFrame(data)

st.set_page_config(layout="wide")
st.title("📞 Dashboard de Performance Operacional")

# Filtros
mes = st.selectbox("Selecione o Mês:", df["Mês"].unique())
filtro = df[df["Mês"] == mes]

# Métricas principais
col1, col2, col3 = st.columns(3)
col1.metric("📊 Média de Vendas", round(filtro["Vendas"].mean(), 2))
col2.metric("⏱️ TMA Médio (s)", round(filtro["TMA"].mean(), 2))
col3.metric("✔️ Qualidade Média (%)", round(filtro["Qualidade"].mean(), 2))

# Gráfico de Vendas por Operador
fig_vendas = px.bar(filtro, x="Operador", y="Vendas", color="Operador", title="Vendas por Operador")
st.plotly_chart(fig_vendas, use_container_width=True)

# Gráfico TMA
fig_tma = px.line(filtro, x="Operador", y="TMA", markers=True, title="TMA por Operador")
st.plotly_chart(fig_tma, use_container_width=True)
