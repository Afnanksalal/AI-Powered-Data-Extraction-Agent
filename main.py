import streamlit as st
from dashboard import dashboard
from data_processing import process_data
from search_and_extract import search_and_extract, SerpAPIError
from llm_integration import process_with_llm, GroqError
from utils import load_config
import pandas as pd

# Load configuration from config.yaml
config = load_config("config.yaml")

st.title("AI Agent for Data Extraction")

# Initialize the dashboard to get user inputs (CSV upload, column selection, query prompt)
dashboard()

# When the "Run Extraction" button is clicked
if st.button("Run Extraction"):
    with st.spinner("Running extraction..."):  # Display a spinner while processing
        try:
            # Load the data from the uploaded CSV
            df = process_data()
            if df is None:
                st.error("No data loaded. Please upload a CSV.")
                st.stop()  # Stop execution if no data is loaded

            # Retrieve user inputs from the session state
            selected_column = st.session_state.get("selected_column")
            query_prompt = st.session_state.get("query_prompt")

            # Validate user inputs
            if not selected_column or not query_prompt:
                st.error("Please select a column and enter a query prompt.")
                st.stop()

            # Initialize an empty list to store extracted data
            extracted_data = []

            # Iterate through each entity in the selected column
            for entity in df[selected_column]:
                try:
                    # Format the query prompt with the current entity
                    query = query_prompt.format(**{selected_column.lower(): entity})
                    
                    # Perform the search and extract search results
                    search_results = search_and_extract(query, config)

                    # Format search results into a string or provide a message if none found
                    if search_results:
                        search_results_text = "\n".join([f"{r.get('title', '')}\n{r.get('snippet', '')}" for r in search_results])
                    else:
                        search_results_text = "No search results found."

                    # Process the query and search results with the LLM
                    extracted_info = process_with_llm(query, search_results_text, config)
                    
                    # Append the extracted information to the list
                    extracted_data.append({"Entity": entity, "Extracted Info": extracted_info})

                except SerpAPIError as e:
                    st.error(f"SerpAPI error for {entity}: {e}")
                    extracted_data.append({"Entity": entity, "Extracted Info": f"SerpAPI Error: {e}"})
                except GroqError as e:
                    st.error(f"Groq error for {entity}: {e}")
                    extracted_data.append({"Entity": entity, "Extracted Info": f"Groq Error: {e}"})
                except Exception as e:
                    st.error(f"Error processing {entity}: {e}")
                    extracted_data.append({"Entity": entity, "Extracted Info": f"Error: {e}"})

            # Display the extracted data in a Streamlit dataframe
            st.subheader("Extracted Data")
            st.dataframe(pd.DataFrame(extracted_data))

        except Exception as e:
            st.error(f"An error occurred: {e}")
