import streamlit
import snowflake.connector

streamlit.title('Athleisure Catalog')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select current_user(), current_account(), current_region()")

my_data_row = my_cur.fetchone()

streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
