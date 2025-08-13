import streamlit as st
import numpy as np
import os
import shutil

opt_select = st.selectbox(
    "Please select from one of the options",
    ("Abs", "Bgf")
)

if opt_select!="Upload":
    with st.form("upload-form", clear_on_submit=True):
        st.write("New created.")
        uploaded_file = st.file_uploader("Upload text file", type=["txt"])
        submitted= st.form_submit_button()
        print("AAA",uploaded_file)
        if uploaded_file is not None:
            st.write("Success.")

        else:
            st.warning("No Selection")
