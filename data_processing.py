import pandas as pd
import streamlit as st

def process_data():
    """Loads the data from the uploaded CSV file stored in the session state.

    Returns:
        pandas.DataFrame: The loaded DataFrame, or None if no file is uploaded.
    """
    if "uploaded_df" in st.session_state:
        return st.session_state["uploaded_df"]
    return None
