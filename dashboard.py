import streamlit as st
import pandas as pd

def dashboard():
    """Creates the Streamlit dashboard for user interaction."""
    uploaded_file = st.file_uploader("Upload a CSV File", type=["csv"])
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            st.session_state["uploaded_df"] = df
            st.write("Uploaded CSV file preview:")
            st.dataframe(df.head())
        except Exception as e:
            st.error(f"Error reading CSV: {e}")

    if "uploaded_df" in st.session_state:
        df = st.session_state["uploaded_df"]
        st.session_state["selected_column"] = st.selectbox("Select Column", df.columns.tolist())
        st.session_state["query_prompt"] = st.text_input(
            "Enter Query Prompt (e.g: 'Give me contact details of {company}')",
            value="Give me contact information about {company}"
        )
