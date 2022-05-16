import streamlit as st
import snowflake.connector
import pandas as pd
from PIL import Image

st.set_page_config(page_title = "Füchse Berlin", layout = "wide")

# Check and printing sf connections
st.text("Establishing Snowflake connection...")
my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
st.text("User | Account | Region")
my_cur.execute("SELECT CURRENT_USER, CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
st.text(my_data_row)


# actual team info
st.title('Füchse Berlin | Saison 2021/22')

image = Image.open('kader_berlin.jpg')
st.image(image)

st.header("Teamstatistik")

col1, col2 = st.columns(2)

#col1.subheader('Platzierungen Saison 2021/22')
col1.markdown('**Tabellenplatz**: 4️⃣')
col1.markdown('**Siege** | **Unentschieden** | **Niederlagen** : 21 | 4 | 4')
col1.markdown('**Tore**: 858')
col1.markdown("**Gegentore**: 753")
col1.markdown("**Differenz**: 105")
col1.markdown("**Bester 7m-Schütze**: Hans Lindberg(108/118/91.5%)")
col1.markdown("**Sünder**: Mijajlo Marsenic(57)")
col1.markdown("**Ticketverkäufe**: 95240")


tabellenstand = Image.open('tabelle_hist_berlin.png')
col2.image(tabellenstand)



st.header("Spieler Gesamtstatistik")

#st.text("Spaltennamen | 0️⃣: Nachname, 1️⃣: Vorname, 2️⃣: POS, 3️⃣: S, 4️⃣: T, 5️⃣: FW, 6️⃣: FT, 7️⃣: 7M")
#st.text("8️⃣: %, 9️⃣: AS, 1️⃣0️⃣: TF, 1️⃣1️⃣: ST, 1️⃣2️⃣: BL, 1️⃣3️⃣: GK, 1️⃣4️⃣: 2M, 1️⃣5️⃣: RK, 1️⃣6️⃣: BK")
#my_cur.execute("SELECT * FROM kader_berlin")
#my_data_rows = my_cur.fetchall()
#data_berlin = st.dataframe(my_data_rows)

# Spielwiese

df = pd.read_csv("kader_berlin_index_false.csv")
rad = st.sidebar.radio("Navigation",["Gesamtansicht","Gefilterte Ansicht"])

# Sidebar

if rad == "Gesamtansicht":
  st.text("Erstansicht absteigend nach geworfenen Toren sortiert")
  st.dataframe(df)

if rad == "Gefilterte Ansicht":
  st.text("Erstansicht zeigt Stammtorhüter")
  st.sidebar.header("Hier Filter wählen:")

  positionen = st.sidebar.multiselect("Spielposition (Angriffsmodus):", options = df["Position"].unique(), default = df["Positionen"].unique())

  nachname = st.sidebar.multiselect("Spieler (Nachname):",options = df["Nachname"].unique(), default = ["Milosavljev"])

  df_selection = df.query("Position == @positionen & Nachname == @nachname")

  st.dataframe(df_selection)






