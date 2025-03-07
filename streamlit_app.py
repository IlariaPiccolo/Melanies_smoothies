# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

helpful_links = [
    "https://docs.streamlit.io",
    "https://docs.snowflake.com/en/developer-guide/streamlit/about-streamlit",
    "https://github.com/Snowflake-Labs/snowflake-demo-streamlit",
    "https://docs.snowflake.com/en/release-notes/streamlit-in-snowflake"
]

# Write directly to the app
st.title(":cup_with_straw: Customize your smoothie :cup_with_straw:")
st.write(
    f"""Choose the fruit you want in your custom smoothie!!
    """
)



name_on_order = st.text_input("Name on Smoothie:")
st.write("The name on your smoothie will be:", name_on_order)

#option = st.selectbox(
#    "What's your favourite fruit?",
#    ("Banana", "Strawberries", "Peaches"),
#)


cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)



ingredients_list = st.multiselect(
    'choose up to 5 ingredients:',
    my_dataframe,
    max_selections = 5
)


if ingredients_list:
    ingredients_string = ''


    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

    my_insert_stmt = "insert into smoothies.public.orders(ingredients, name_on_order) values(\'" + ingredients_string + "\',\'" + name_on_order + "\')"

    #st.write(my_insert_stmt)
    #st.stop()

    #time_to_insert = st.button('Submit Order')
    
    if st.button('Submit Order'):
        session.sql(my_insert_stmt).collect()
        
        st.success('Your Smoothie is ordered!', icon="✅")

import requests
smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
st.text(smoothiefroot_response)
    
    #st.write (ingredients_string)
    #st.write(my_insert_stmt)

