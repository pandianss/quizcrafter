# Imported Libraries
import streamlit as st
import time

# Pages
warning_message = 'Careful, you are about to reset the entire match'

def disable_button():
    st.session_state['disabled']=b

def cancel_warning():
    popup_slot = st.empty()
    popup_slot.write(warning_message)
    time.sleep(500)
    popup_slot.empty()

def page1():
    st.write('# Cricket')
    cricket_button = st.button('Start Match!', on_click=disable_button)
    st.write('Content for Page1')
    if cricket_button:

        page1_1()


def page1_1():
    st.write('Let the games begin!!!')
    cricket_button_cancel = st.button('Cancel Match!')
    if cricket_button_cancel:
        cancel_warning()


def page2():
    st.metric('Matches played', '100 sets', '2 sets')
    st.write('# Badminton')
    st.write('Content for Page2')

def page3():
    st.metric('Matches played', '30 games', '2 games')
    st.write('# Football')
    st.write('Content for Page3')

page = st.sidebar.radio('Go to', ['Cricket', 'Badminton', 'Football'])

if page == 'Cricket':
    page1()

elif page == 'Badminton':
    page2()

elif page == 'Football':
    page3()
