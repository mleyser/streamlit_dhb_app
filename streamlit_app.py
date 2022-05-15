import streamlit
import snowflake.connector
import pandas as pd

streamlit.title('DHB Kader der Kontrahenten')
streamlit.header('Füchse Berlin')
streamlit.text('Hier platzieren wir die Kaderliste der Füchse Berlin.')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

