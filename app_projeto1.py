import streamlit as  st
import pandas as pd


st.title("Hello Streamlit")
st.write("Este é o meu primeiro app com Streamlit!")
st.header("Este é um header")
st.subheader("Este é um subheader4")
st.text("Este é um texto simples")
st.markdown("Este é um **6666tesxto em negrito**")
st.latex(r'''e^{i\pi} + 1 = 0''')

df =pd.DataFrame({
    'Nome': ['Alice', 'Bob', 'Charlie'],
    'Idade': [25, 30, 35],
    'Cidade': ['Nova York', 'Los Angeles', 'Chicago']
    'Salario': [70000, 80000, 90000]
})

st.dataframe(df)
st.table(df)



