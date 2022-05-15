import streamlit
import snowflake.connector
import pandas as pd

streamlit.title('DHB Kader der Kontrahenten')
streamlit.header('Füchse Berlin')
streamlit.text('Hier platzieren wir die Kaderliste der Füchse Berlin.')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
