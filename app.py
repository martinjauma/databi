import streamlit as st
import pandas as pd
from pymongo import MongoClient

# --- conexión MongoDB ---
# Accedé al secreto
mongo_url = st.secrets["MONGO_URL"]

# Conectá a MongoDB
client = MongoClient(mongo_url)
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
