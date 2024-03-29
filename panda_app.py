import pandas as pd
import streamlit as st

st.title('My Neighbours favourite daily')
st.header('My Favourite Breakfast')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = st.multiselect('Pick some fruits:',list(my_fruit_list.index))
Fruits_to_show = my_fruit_list.loc[fruits_selected]
def paginate_dataframe(dataframe, page_size, page_num):
    page_size = page_size
    if page_size is None:
        return None
    offset = page_size*(page_num-1)
    return dataframe[offset:offset + page_size]
st.dataframe(Fruits_to_show)

st.header("Fruityvice Fruit Advice!")
fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# The next line will display the json in table format
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# display the result in data frame
st.dataframe(fruityvice_normalized)
