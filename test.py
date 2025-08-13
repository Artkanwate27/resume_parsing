import streamlit as st

opt_select = st.selectbox(
    "Please select from one of the options",
    ("Upload", "Abs", "Bgf")
)

if opt_select == "Upload":
    with st.form("upload-form", clear_on_submit=True):
        st.write("Please upload a text file.")
        uploaded_file = st.file_uploader("Upload text file", type=["txt"])
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            if uploaded_file is not None:
                st.success("File uploaded successfully!")
            else:
                st.warning("No file selected. Please upload a text file.")
else:
    st.write(f"You selected option: {opt_select}")
