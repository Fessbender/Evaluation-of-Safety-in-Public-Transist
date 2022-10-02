import csv
import pandas as pd
import streamlit as st


st.set_page_config(page_title='TRANSPORT SAFETY APP')
st.header('SAFETY ANALYSIS')


st.subheader('Was the tutorial helpful?')


### --- LOAD DATAFRAME
CSV_file = "G:/Transport Safety Project/Clean Data.csv"
sheet_name = 'Clean Data'

df = pd.read_CSV(CSV_file,
                   sheet_name=sheet_name,
                   usecols='A:I',
                   header=7)



