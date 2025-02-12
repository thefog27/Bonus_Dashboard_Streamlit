import pandas as pd
import streamlit as st
from datetime import date

st.title('Explanation')


st.subheader('Please Note', divider= 'gray')
st.text('• The upload file must be an excel file.  \n • Do not change the format (names, tables, tabs) of the upload file. \n • For testing purposes, the excel file  „Test_Data_Bonus‟ from the Guthub repository can be used.')
st.text('Disregarding the above points can lead to errors.')

data = {
    'First_day_of_week': pd.to_datetime(['03.02.2025', '10.02.2025', '17.02.2025'], format='%d.%m.%Y').date,
    'Calender_week': ['12', '33', '45'],
    'Working_hours': [42.45, 50.20, 35.00]
}

df = pd.DataFrame(data)
df['Working_hours'] = df['Working_hours'].apply(lambda x: f"{x:.2f}")
st.text('Example Sample Data')
st.dataframe(df) 


st.subheader('About this project', divider= 'gray')
st.text('The idea for this project was inspired by my girlfriend. \nIn her job, she can earn commission, i.e. a bonus, when she sells certain services to customers. This bonus is calculated on the basis of hours worked. \nIn order to get a better overview of her earned bonus, she asked me to create an excel file for her that can calculate the bonus automatically. Over time, this excel file has turned into a python project that uses the streamlit library to realise an interactive dashboard. \nMy girlfriend still uses the dashboard regularly today.')


st.subheader('Bonus System', divider= 'gray')

data = {
    'Working Hours': ['20-25', '26-28', '28 >'],
    'Bonus %*': ['15 %', '20 %', '25 %'], 
    'Bonus €': [19.50, 26.00, 32.50]
}

df = pd.DataFrame(data)
df['Bonus €'] = df['Bonus €'].apply(lambda x: f"{x:.2f}")
st.dataframe(df) 
st.text('*Hourly Rate: 130 €')


st.subheader('What does the term „Ichiban‟ mean ?', divider= 'gray')
st.text('Ichiban is a Japanese word and means as much as: number one; first; best. \nIn the context of this dashboard, the term Ichiban is used to indicate a high score. For example, the highest number of hours worked/the largest bonus amount ever in a calender week or the most successful calendar week ever.')

search = st.secrets['search']
st.image(search, caption = 'google search for ichiban', width = 500)
