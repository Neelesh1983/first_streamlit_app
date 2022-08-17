import streamlit as st
import snowflake.connector as stc
cont1 = st.container()
cont1.title('this is container area')
st.header('Breakfast Menu')
st.text('Omega 3 & Blueberry Oatmeal')
st.text('Kale, Spinach & Rocket Smoothie')
st.text('Hard-Boiled Free-Range Egg')

st.title ("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')
st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)
st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')
st.balloons()
st.progress(10)
## with st.spinner('Wait for it...'):
##   time.sleep(10)
    
#st.success("You did it !")
#st.error("Error")
#st.warning("Warning")
#st.info("It's easy to build a streamlit app")
#st.exception(RuntimeError("RuntimeError exception"))

## sidebar, spinner, echo 

st.sidebar.title('This is sidebar')
st.sidebar.button('click')

my_cnx = stc.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select S_STORE_ID from store")
my_data_row = my_cur.fetchall()
st.header("List of customers")
st.dataframe(my_data_rows)

    

