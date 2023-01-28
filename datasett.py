# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 15:45:18 2023

@author: SAAD COMMUNICATION
"""

import pandas as pd
import streamlit as st

#file = r'C:\Users\SAAD COMMUNICATION\Desktop\week 2\Billionaire.csv'

#readingg the file

df=pd.read_csv(Billionaires.csv)
df2=st.file_uploader(label="Upload Your file", type="csv")
#find the count of billioners by country
bill_count=df.groupby('Country')['Name'].count().sort_values().head(20)

#st.bar_chart(bill_count)

#find most popular source of income
pop_sou=df.groupby("Source")['Name'].count()


NetWorth_new=df['NetWorth'].apply(lambda x:float(x.replace('$','').replace('B','')))
#interaction

all_country=df['Country'].unique()
selection=st.selectbox("Select Country",all_country)
subset=df[df['Country']==selection]
st.dataframe(subset)

col1,col2=st.columns(2)
#colulmn 1
#display on streamlit
selected_country=col1.selectbox("Select Your Country",all_country)
#subset on selected country
subset_country=df[df["Country"]==selected_country]

#get unique sources from selected country
sources=sorted(subset_country["Source"].unique())
#display multi select optionon source
selected_source=col1.multiselect("Select Source of income",sources)
#subset on selected sources
subset_source=subset_country[subset_country["Source"].isin(selected_source)]

#Column2
main_string='{} - Billioners'.format(selected_country)
col2.header(main_string)
col2.dataframe(subset_country)
col2.header("Source Wise Info")
col2.dataframe(subset_source)
