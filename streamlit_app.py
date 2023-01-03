import streamlit
import snowflake.connector
import pandas

streamlit.title('Athleisure Catalog')

# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# run a snowflake query and put it all in a var called my_catalog
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

#put the data into a dataframe
df = pandas.DataFrame(my_catalog)

#temp write the dataframe to the page so I can see what I am working with
#streamlit.write(df)

# put first columns into a list
color_list = df[0].values.tolist()
#print(color_list)

#put a picklist here so they can pick the color
option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))

#Image caption
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'

#use option selected to get info from database
my_cur.execute("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where color_or_style = '" + option + "';")
df2 = my_cur.fetchone()

streamlit.image(df2[0], width=400, caption= product_caption)

streamlit.write('Price: ', df2[1])
streamlit.write('Sizes available: ', df2[2])
streamlit.write(df2[3])
