import streamlit as st

# Streamlit app title
st.title('Document Uploader')

# File uploader widget
uploaded_file = st.file_uploader("Upload a document", type=['txt', 'pdf', 'docx'])

# Check if a file was uploaded
if uploaded_file is not None:
    # Display the file details
    file_details = {"Filename": uploaded_file.name, "FileType": uploaded_file.type}
    st.write(file_details)

    # Optionally, you can read and display the contents of the file
    file_contents = uploaded_file.read()
    st.write("File contents:")
    st.write(file_contents)
