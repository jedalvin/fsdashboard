import streamlit as st
import pandas as pd

# Streamlit app title
st.title('Excel File Uploader and Data Cleaning')

# File uploader widget
uploaded_file = st.file_uploader("Upload an Excel file", type=['xls', 'xlsx'])

# Check if a file was uploaded
if uploaded_file is not None:
    # Read the Excel file into a pandas DataFrame
    try:
        df = pd.read_excel(uploaded_file)
        st.write("Original DataFrame:")
        st.write(df)
        
        # Perform data cleaning (example: removing null values)
        cleaned_df = df.dropna()
        st.write("Cleaned DataFrame (null values removed):")
        st.write(cleaned_df)
        
        # Perform grouping (example: grouping by a specific column)
        grouped_df = cleaned_df.groupby('Category').sum()
        st.write("Grouped DataFrame:")
        st.write(grouped_df)
        
    except Exception as e:
        st.error(f"Error: {e}")
