import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
st.set_page_config(page_title="Dashboard")

st.sidebar.title("upload csv")
uploaded_file=st.sidebar.file_uploader("choose a csv file",type="csv")
st.title("Dashboard for csv")
if uploaded_file:
    df=pd.read_csv(uploaded_file)
    st.success("File Successfully Uploaded")
    st.subheader("data view")
    st.dataframe(df.head())
    #plot
    st.subheader("histogram")
    numeric_col=df.select_dtypes(include=['float64','int64']).columns.tolist()
    selected_Col=st.selectbox("select one",numeric_col)
    fig,ax=plt.subplots()
    df[selected_Col].hist(bins=20,ax=ax)
    ax.set_xlabel(selected_Col)
    ax.set_ylabel("Frequency")
    st.pyplot(fig)