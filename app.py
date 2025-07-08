import streamlit as st
import pandas as pd
import os
from pymongo import MongoClient

# --- conexión MongoDB ---
# Accedé al secreto
mongo_url = st.secrets.get("MONGO_URL", os.getenv("MONGO_URL"))

# Conectá a MongoDB
client = MongoClient(mongo_url)
db = client["SRA"]
collection = db["DATA"]

# --- Obtener estadísticas de la colección ---
stats = db.command("collstats", "DATA")

# Tamaño total en bytes → lo pasamos a MB (dividido 1024²)
size_mb = stats["size"] / (1024 * 1024)


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
st.write(f"Peso total de los documentos: {size_mb:.2f} MB")

st.dataframe(df)
