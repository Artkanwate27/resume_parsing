import streamlit as st

opt_select = st.selectbox(
    "Please select from one of the options",
    ("Upload Resume", "Use Dummy Resume")
)

if opt_select == "Upload Resume":
    with st.form("upload-form", clear_on_submit=True):
        st.write("Please upload your resume (PDF format).")
        uploaded_file = st.file_uploader("Upload resume", type=["pdf"])
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            if uploaded_file is not None:
                st.success("Resume uploaded successfully!")
            else:
                st.warning("Please select a file before submitting.")

elif opt_select == "Use Dummy Resume":
    st.write("Using preloaded dummy resume for testing.")
    # yahan tum dummy_resume.pdf ka path use kar sakte ho
