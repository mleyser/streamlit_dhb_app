import streamlit as st
import snowflake.connector
import pandas as pd
from PIL import Image

st.set_page_config(page_title = "Füchse Berlin", layout = "wide")

# Check and printing sf connections
st.text("Establishing Snowflake connection")
my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
st.text("User | Account | Region")
my_cur.execute("SELECT CURRENT_USER, CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
st.text(my_data_row)


# actual team info
st.title('Kader | Saison 2021/22')

image = Image.open('kader_berlin.jpg')
st.image(image)


st.header("Spieler Gesamtstatistik")


st.text("Spaltennamen | 0: Nachname, 1: Vorname, 2: POS, 3: S, 4: T, 5: FW, 6: FT, 7: 7M")
st.text("8: %, 9: AS, 10: TF, 11: ST, 12: BL, 13: GK, 14: 2M, 15: RK, 16: BK")
my_cur.execute("SELECT * FROM kader_berlin")
my_data_rows = my_cur.fetchall()
data_berlin = st.dataframe(my_data_rows)





