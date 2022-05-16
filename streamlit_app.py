import streamlit as st
import snowflake.connector
import pandas as pd



st.title('DHB Kader der Kontrahenten')
st.header('Füchse Berlin')
st.text('Hier platzieren wir die Kaderliste der Füchse Berlin.')

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
st.text("Hello from Snowflake:")
st.text(my_data_row)

my_cur.execute("SELECT * FROM kader_berlin")
my_data_rows = my_cur.fetchall()
data_berlin = st.table(pd.DataFrame(my_data_rows, columns = ["Nachname","Vorname","Position","Spiele","Tore","Fehlwürfe","Feldtore","7-Meter-Tore","Wurfquote","Assists","Technische Fehler","Steals","Blocks","Gelbe Karten","2 min Strafen","Rote Karten", "Blaue Karten"]))





