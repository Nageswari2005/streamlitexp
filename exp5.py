import pandas as pd
import streamlit as st
from pymongo import MongoClient
import random 
import time
import os
from datetime import datetime

MONGO_URL="mongodb://localhost:27017/"
DB_NAME="streamlit_db"
COLLECTION_NAME="csv_data"
csv_file="data.csv"
refresh_interval=20
client=MongoClient(MONGO_URL)
db=client[DB_NAME]
collection=db[COLLECTION_NAME]
def create_and_save_date():
    new_data={
        'timestamp':datetime.now().strftime("%Y-%m-%d %H:%M:%S"),'value':round(random.uniform(50,150),2)
    }
    df_new=pd.DataFrame([new_data])
    if not os.path.exists(csv_file):
        df_new.to_csv(csv_file,index=False)
    else:
        df_new.to_csv(csv_file,mode="a",header=False,index=False)
def insert_csv_to_db():
    if not os.path.exists(csv_file):
        df=pd.read_csv(csv_file)
        records=st.to_dict(orient='recors')
        if records:
            collection.insert_many(records)
def read_from_db():
    cursor=collection.find()
    data=list(cursor)
    if data:
        df=pd.DataFrame(data)
        df.drop(columns=["_id"],inplace=True)
        return df
    st.set_page_config(page_title="dashboard")
    st.title("fetch data from mongodb")
    placeholder=st.empty()
    while True:
        create_and_save_date()
        insert_csv_to_db
        df=read_from_db
        st.dataframe(df)
        st.write(f"Refreshing in{refresh_interval}")
    time.sleep(refresh_interval)
