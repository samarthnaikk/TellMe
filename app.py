import streamlit as st
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

def get_pdf_text_chunks(pdfs):
    all_texts = []
    for pdf in pdfs:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(pdf.read())
            tmp_path = tmp_file.name

        loader = PyPDFLoader(tmp_path)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        all_texts.extend(text_splitter.split_documents(documents))
    return all_texts

def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(text_chunks, embeddings)
    return vectorstore

def get_conversational_chain(vectorstore):
    llm = OllamaLLM(model="llama3")
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vectorstore.as_retriever(), memory=memory)
    return chain

def main():
    st.set_page_config("Ask your PDFs 💬")
    st.header("Ask your PDFs 💬")

    pdfs = st.file_uploader("Upload your PDFs", type="pdf", accept_multiple_files=True)

    if pdfs:
        text_chunks = get_pdf_text_chunks(pdfs)
        vectorstore = get_vectorstore(text_chunks)
        st.session_state.chain = get_conversational_chain(vectorstore)
        st.success("PDFs processed successfully! Ask your questions below 👇")

    if "chain" in st.session_state:
        question = st.text_input("Ask a question about your PDFs:")
        if question:
            response = st.session_state.chain.run(question)
            st.write(response)

if __name__ == "__main__":
    main()
