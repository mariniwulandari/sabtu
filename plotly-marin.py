import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Visualisasi Data Diamond")
st.title("oleh Marin")

df = pd.read_csv('data/diamonds.csv', sep =',')

st.write("## 5 data pertama")
st.write(df.head())

st.write("## Histogram Harga Diamond")
plot = px.histogram(
    df,
    x="price",
    title="Histogram Harga Diamond"
)
plot.update_layout(
    xaxis_title = "Harga",
    yaxis_title = "Jumlah"
)
st.plotly_chart(plot)

st.write("## Histogram Color")
plot_color = px.histogram(
    df,
    x = "color",
    title = "Histogram Warna Diamond"
)
plot_color.update_layout(
    xaxis_title = "Warna",
    yaxis_title = "Jumlah"
)
st.plotly_chart(plot_color)
st.write("## Line chart dimensi x, y, dan z")
plot_dimensi = px.line(
    df,
    y = ["x","y","z"],
    title = "Dimensi x, y, z"
)
st.plotly_chart(plot_dimensi)
