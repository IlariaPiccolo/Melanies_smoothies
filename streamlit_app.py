# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

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


#option = st.selectbox(
#    "What's your favourite fruit?",
#    ("Banana", "Strawberries", "Peaches"),
#)

from snowflake.snowpark.functions import col

session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)



ingredients_list = st.multiselect(
    'choose up to 5 ingredients:',
    my_dataframe
)


if ingredients_list:
    ingredients_string = ''


    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """')"""

    time_to_insert = st.button('Submit Order')

    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")
    
    
    #st.write (ingredients_string)
    #st.write(my_insert_stmt)
