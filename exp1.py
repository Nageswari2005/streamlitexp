import pandas as pd
import streamlit as st
data_set=pd.DataFrame(
    {
        'month':['jan','feb','mar'],
        'food':[4000,3500,3200],
        'ent':[4000,500,2500],
        'miscell':[6000,4500,3000]
    })
print(data_set)
data_set.set_index('month',inplace=True)
st.bar_chart(data_set) 