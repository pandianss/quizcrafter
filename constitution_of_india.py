import streamlit as st

with open('countries.txt', 'r') as file:
    countries = file.readlines()

def comment():
    with st.form('Customer feedback form'):
        name_input = st.text_input('Name:', value='')
        email_input = st.text_input('Valid email id', value='')
        Country_input = st.selectbox('Country',countries)
        my_comment = st.text_area('Comment',height=200)
        comment_button = st.form_submit_button('Submit comment')

def main():
    st.set_page_config(page_title='Constition of India')
    st.sidebar.title('Navigation')
    b1 = st.sidebar.button('Learn - Zoom Mode')
    b2 = st.sidebar.button('Quiz')
    b1 = st.sidebar.button('Leaderboard')
    b1 = st.sidebar.button('Analytics')

    comment()

if __name__ == '__main__':
    main()