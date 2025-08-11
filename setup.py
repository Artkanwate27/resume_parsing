from setuptools import setup, find_packages

setup(
    name="job_screener",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your requirements here (same as requirements.txt)
        "streamlit",
        "pypdf2",
        "pdfplumber",
        "nltk",
        "sentence-transformers",
        "python-dotenv",
        "fastapi",
        "uvicorn",
        "sqlalchemy"
    ],
)
