import csv
import pandas as pd
import streamlit as st


st.write ("""

# Transport Safety App

This web app demonstrates Safety of Transport dataset collected to document security pain points and strategies adopted by different cities in the world to ensure inclusive development in public transit systems""")


try

csv_file= "G:/Transport Safety Project/Clean Data.csv"


data= pd.read_csv (csv_file)



Gender_Select = st.multiselect('gender:',
                                    gender,
                                    default=gender)