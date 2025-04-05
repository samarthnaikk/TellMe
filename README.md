# MultiPDF Chat App

This project is inspired by the MultiPDF Chat App tutorial on YouTube. While the original version uses OpenAI's API, this implementation is designed to work locally using llama3 or other compatible language models(Ollama).

## Introduction

The MultiPDF Chat App is a Python application that allows users to interact with multiple PDF documents using natural language queries. It processes the contents of uploaded PDFs and provides accurate responses based on the information extracted from them.

This application uses a local language model to analyze and answer questions, making it suitable for offline and private use cases. It will only respond to queries that are relevant to the content of the loaded PDFs.

## How It Works

1. **PDF Loading**: The app reads multiple PDF documents and extracts their text content.
2. **Text Chunking**: The extracted text is divided into smaller, manageable chunks.
3. **Language Model Processing**: A local language model generates vector representations (embeddings) of each text chunk.
4. **Similarity Matching**: The application compares the user's question to the text chunks and selects the most relevant ones.
5. **Response Generation**: The selected chunks are passed to the language model, which generates a response based on the content of the PDFs.

## Dependencies and Installation

To install and run the MultiPDF Chat App:

   ```bash
   git clone git@github.com:samarthnaikk/TellMe.git
   cd TellMe
   pip install -r requirements.txt
   streamlit run app.py
   ```
Once launched, the web interface will open in your browser. Follow the instructions to upload multiple PDF files. You can then interact with the documents through the chat interface by asking questions in natural language.

## Credits

This project is inspired by and builds upon the work by [Alejandro A.](https://github.com/alejandro-ao).  
We acknowledge and appreciate the foundational ideas and structure provided in their original implementation.
