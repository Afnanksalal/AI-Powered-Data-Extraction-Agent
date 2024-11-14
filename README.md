# AI-Powered Data Extraction Agent

This project demonstrates an AI-powered data extraction agent that uses SerpAPI for web searching and Groq's LLM for information extraction.  It provides a Streamlit-based interface for users to upload CSV data, specify a query prompt, and extract targeted information from the web.

## Features

* **CSV Data Upload:**  Users can upload their CSV data through a user-friendly interface.
* **Dynamic Query Prompts:**  The application allows users to define flexible query prompts using placeholders that correspond to column names in the CSV.
* **SerpAPI Integration:** Leverages SerpAPI for performing web searches based on user queries.
* **Groq LLM Integration:** Uses Groq's Large Language Model (LLM) to extract specific information from search results.
* **Concise and Plaintext Output:**  The LLM is instructed to provide concise, plain text answers without extra formatting or explanations.
* **Error Handling:** Robust error handling ensures that issues with API calls or data processing are caught and displayed to the user.
* **Streamlit Interface:** Provides an interactive and easy-to-use web application for data extraction.


## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Afnanksalal/AI-Powered-Data-Extraction-Agent
   cd AI-Powered-Data-Extraction-Agent
   ```

2. **Create and Activate a Virtual Environment:** (Recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Linux/macOS
   venv\Scripts\activate  # On Windows
   ```

3. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Modify `config.yaml`:**  Replace values in `config.yaml` in the project's root directory with your API keys:

   ```yaml
   serpapi_api_key: YOUR_SERPAPI_API_KEY
   groq_api_key: YOUR_GROQ_API_KEY
   ```

## Usage

1. **Run the Streamlit App:**
   ```bash
   streamlit run main.py
   ```

2. **Upload CSV Data:** Use the file uploader in the Streamlit app to upload your CSV file.

3. **Select Column:** Choose the column from your CSV that you want to use for the queries.

4. **Enter Query Prompt:**  Enter a query prompt.  Use curly braces `{}` as placeholders for the values from the selected column. For example:
   - If your column is named "company": `Give me contact details of {company}`

5. **Run Extraction:** Click the "Run Extraction" button to start the data extraction process.


## Example CSV Files

You can find example CSV file (`example.csv`) in the repository to test the application.


## Project Structure

* `main.py`: The main Streamlit application file.
* `search_and_extract.py`: Handles web searches using SerpAPI.
* `llm_integration.py`:  Handles interaction with the Groq LLM.
* `dashboard.py`: Creates the Streamlit dashboard components.
* `utils.py`:  Contains utility functions (e.g., loading configuration).
* `data_processing.py`: Handles data loading.
* `config.yaml`:  Stores API keys and configuration


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request.


## Acknowledgements

* **SerpAPI:**  Used for web search functionality.  [https://serpapi.com/](https://serpapi.com/)
* **Groq:** Used for LLM-powered information extraction. [https://groq.com/](https://groq.com/)
* **Streamlit:** Used for creating the interactive web application. [https://streamlit.io/](https://streamlit.io/)
