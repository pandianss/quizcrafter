import streamlit as st

with open('assets\\toast.txt', 'r') as messages:
    toast_message = messages.readline()

st.set_page_config(page_title='Comment . QuizCrafter',page_icon='assets\\color.svg')    
st.toast(toast_message)
st.sidebar.chat_input('Ask something')

with open('assets\\countries.txt', 'r') as file:
    countries = file.readlines()

def comment():
    with st.form('Please give your valuable suggestions to improve the site'):
        name_input = st.text_input('Name:', value='')
        email_input = st.text_input('Valid email id:', value='')
        Country_input = st.selectbox('Country:',countries)
        my_comment = st.text_area('Comment:',height=200)
        comment_button = st.form_submit_button('Submit comment')


st.title('Suggestion box')
st.caption('Critical comments / suggestions to improve the site are welcome')
comment()
