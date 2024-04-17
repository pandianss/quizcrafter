import streamlit as st
with open('assets\\toast.txt', 'r') as messages:
    toast_message = messages.readline()
st.set_page_config(page_title='Compete . QuizCrafter',page_icon='assets\\color.svg')    
st.header('Compete')
st.toast(toast_message)
st.sidebar.ch 