import streamlit as st
import pickle
import pandas as pd


pipe = pickle.load(open('food.pkl','rb'))

st.title('Food taste predictor')

col1, col2 = st.columns(2)

with col1:
    addition_time = st.number_input('Additional Time')
with col2:
    servings = st.number_input('No of people you served the dish')



col3,col4,col5 = st.columns(3)

with col3:
    prep_time = st.number_input('Preparation Time')
with col4:
    cook_time = st.number_input('Cooking Time')
with col5:
    total_time = st.number_input('Total Time')

calories = st.number_input('Total calories')

col6,col7,col8,col9 = st.columns(4)
with col6:
    fat = st.number_input('Total fat')
with col7:
    carbs = st.number_input('Total carbs')
with col8:
    protine = st.number_input('Total Protein')
with col9:
    rating = st.number_input('Average rating')

if st.button('Your dish will be'):


    input_df = pd.DataFrame(
     {'addition_time': [addition_time], 'servings': [servings],'prep_time':[prep_time], 'cook_time': [cook_time],'total_time': [total_time],
      'calories': [calories], 'fat': [fat], 'carbs': [carbs], 'protine': [protine],'rating': [rating]})
    result = pipe.predict(input_df)
    if result==1:

        st.header("Good")
    else:
        st.header("Bad")

