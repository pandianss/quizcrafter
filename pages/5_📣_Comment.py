import streamlit as st

st.set_page_config(page_title='QuizCrafter/Comment',page_icon='assets\\color.svg')    

with open('countries.txt', 'r') as file:
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
