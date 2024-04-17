from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


def main():
    load_dotenv()
    st.set_page_config(page_title='Ask your pdf')
    st.header('Gate')
    pdf = st.file_uploader('Upload File', type='pdf')
    
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()

        text_splitter = CharacterTextSplitter(
            separator='\n',
            chunk_size = 1000,
            chunk_overlap = 200,
            length_function = len
        )
        chunks = text_splitter.split_text(text)

        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks,embeddings)

        user_question = st.text_input('Ask me about the Constitution')
        if user_question:
            docs = knowledge_base.search(user_question)
            st.write(docs)

if __name__ == '__main__':
    main()