from dotenv import load_dotenv
import streamlit as st

def main():
    print(os.getenv('OPENAI_API_KEY'))

if __name__ == '__main__':
    main()