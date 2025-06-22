import streamlit as st
import pandas as pd

# File uploader
uploaded_file = st.file_uploader("Drag and drop a CSV file here", type=["xlsx"])

# Process uploaded file
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("✅ File uploaded successfully!")
    st.dataframe(df)
