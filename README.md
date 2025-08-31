PDF Chat Agent
==============

This project is a chat agent that allows you to have a conversation with a PDF document. It leverages the LangChain framework to perform Retrieval-Augmented Generation (RAG) using a local FAISS vector store.

The agent works by:

1.  Loading a PDF document.

2.  Splitting the document's content into smaller, manageable chunks.

3.  Creating vector embeddings of these chunks using OpenAI's embedding model.

4.  Storing the embeddings and their associated text in a local FAISS vector store for efficient similarity searching.

5.  When a user asks a question, the agent retrieves the most relevant chunks from the vector store.

6.  The retrieved chunks are then passed to a large language model (LLM) as context, allowing it to generate an accurate and informed answer.

Prerequisites
-------------

Before running this project, ensure you have the following installed:

-   **Python 3.10+**

-   **OpenAI API Key**: You will need a valid API key to use OpenAI's embedding model and Chat models.

Installation
------------

1.  **Clone the repository:**

    ```
    git clone https://github.com/bk-12346/PDF_chat_agent
    cd PDF_chat_agent

    ```

2.  **Create and activate a virtual environment:**

    ```
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate

    ```

3.  **Install the required packages using pip:

    ```
    pip install -r requirements.txt

    ```

Usage
-----

1.  **Place your PDF file** in the project directory and update the `path` variable in `main.py` to point to your document.

2.  **Set your OpenAI API key:** You can set the API key directly in the script as you have done, or for better security, use an environment variable. If using an environment variable, ensure you have a `.env` file with `OPENAI_API_KEY="your_api_key_here"` and load it in the script using `python-dotenv`.

3.  **Run the script:**

    ```
    python main.py

    ```

The script will:

-   Load the PDF.

-   Split, embed, and save the vector store locally.

-   Load the vector store from the local files.

-   Execute a sample query and print the answer from the LLM. You can modify the query in the `main.py` file
