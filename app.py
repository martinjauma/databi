import streamlit as st
import pandas as pd
from pymongo import MongoClient

# --- conexión MongoDB ---
uri = "mongodb+srv://martinjauma:SRADATAFULL@sra.zzkpnxj.mongodb.net/SRA"
client = MongoClient(uri)

# --- elegimos base y colección ---
db = client["SRA"]
collection = db["DATA"]

# --- consultamos todos los documentos ---
# (limitamos por las dudas a 1000 para no reventar la app)
# data = list(collection.find().limit(1000))
# --- consultamos todos los documentos ---
data = list(collection.find())


# --- pasamos a DataFrame ---
df = pd.DataFrame(data)

# --- mostramos con Streamlit ---
st.title("SRA Data Viewer")
st.write(f"Documentos en la colección: {collection.count_documents({})}")
st.dataframe(df)
