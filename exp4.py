import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import json
st.set_page_config(page_title="reading json data")
st.sidebar.title("upload json file")
uploaded_file=st.sidebar.file_uploader("upload json format",type="json")
if uploaded_file:
    st.success("file uploaded")
    data=json.load(uploaded_file)
    df=pd.DataFrame(data)
    st.success("convert to df")
    st.dataframe(df)
    numeric_col=df.select_dtypes(include=["float64","int64"]).columns
    if not numeric_col.empty:
        st.subheader("summary of subjects")
        st.write(df[numeric_col].describe())
        st.bar_chart(df[numeric_col].mean())
        label_col='post' if 'post' in df.columns else df.columns[0]
        fig,ax=plt.subplots()
        subject=st.selectbox("select sub",numeric_col)
        ax.pie(df[subject],labels=df[label_col],autopct="%1.1f%%")
        st.pyplot(fig)
    if 'name' in df.columns:
        selected=st.multiselect("select name",df['name'].unique())
        if selected:
            st.dataframe(df[df['name'].isin(selected)])