import streamlit
import snowflake.connector
from urllib.error import URLError
import pandas as pd
import requests


streamlit.title('DHB Kader der Kontrahenten')
streamlit.header('Füchse Berlin')
streamlit.text('Hier platzieren wir die Kaderliste der Füchse Berlin.')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cur.execute("select * from kader_berlin")
my_data_rows = my_cur.fetchall()
streamlit.header("Kaderliste Füchse Berlin")
streamlit.dataframe(my_data_rows)
