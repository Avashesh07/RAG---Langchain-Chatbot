# RAG-Langchain-Chatbot

## Overview

This repository contains a chatbot implementation using Retrieval-Augmented Generation (RAG) with Langchain. The project leverages various Python scripts to build and query a knowledge database, utilizing language models for natural language processing tasks.

## Project Structure

- `get_embedding_function.py`: Contains functions to generate embeddings for text data.
- `populate_database.py`: Script to populate the database with embeddings and documents.
- `query_data.py`: Script to query the database and retrieve relevant information using a Streamlit UI.
- `test_rag.py`: Contains test cases to ensure the RAG implementation works as expected.
- `chroma/`: Directory containing the SQLite database and related binary files for data storage.
- `data/`: Directory containing example documents used for populating the database.
  - `MCC-LAWS-OF-CRICKET.pdf`
  - `monopoly.pdf`
  - `ticket_to_ride.pdf`

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Required Python libraries (listed in `requirements.txt` if available)

### Installation

1. Clone the repository:
   git clone https://github.com/yourusername/RAG-Langchain-Chatbot.git
   cd RAG-Langchain-Chatbot
2. Install the required libraries:
  pip install -r requirements.txt

3. Generate Embeddings:
  Run the script to generate embeddings for your documents.
  python get_embedding_function.py

4. Populate Database:
  Use the following script to populate the database with the generated embeddings.
  python populate_database.py

5. Query Data:
  Execute the script to query the database and retrieve relevant information using the Streamlit UI.
  streamlit run query_data.py

6. Run Tests:
  Ensure that everything is working correctly by running the test cases with pytest.
  pytest -s

### Data
The data directory contains example documents used to populate the knowledge database. You can add more documents to this directory as needed.

### Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contact
For any questions or suggestions, please contact me at avashesh.work@gmail.com .
