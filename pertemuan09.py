import streamlit as st

st.title("Kuliah Praktikum Bigdata")
st.write("Marin")
st.write("# Heading 1") 
st.write("## Heading 2") 
st.write("### Heading 3")

pilih1 = st.checkbox('Ya')
pilih2 = st.checkbox('Tidak')

st.write(pilih1)
st.write(pilih2)

makanan = st.radio('Makanan kesukaan',['Sate', 'Nasgor','Bakso']) 
minuman = st.selectbox('Pilih minuman yang akan dipesan',['kopi','teh manis','jus'])

st.write(makanan)
st.write(minuman)

bayar = st.multiselect('Bayar pakai:', ['Tunai', 'Ovo', 'Gopay'])
st.write(bayar)