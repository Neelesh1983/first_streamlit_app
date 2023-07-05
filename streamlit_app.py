import streamlit as st
import snowflake.connector as stc

my_cnx = stc.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select S_STORE_ID from store")
my_data_rows = my_cur.fetchall()
st.header("List of customers")
st.dataframe(my_data_rows)

    

