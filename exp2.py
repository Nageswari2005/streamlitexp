import pandas as pd 
import streamlit as st
st.title("simple data explorer in csv")
uploaded_file=st.file_uploader("upload ur csv",type=["csv"])
if uploaded_file:
    df=pd.read_csv(uploaded_file)
    st.write("display data")
    st.dataframe(df.head())
    col=st.selectbox("select one column",df.columns)
    st.write(df[col].describe())