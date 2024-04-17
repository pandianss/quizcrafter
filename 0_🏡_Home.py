import streamlit as st


def main():
    with open('assets\\toast.txt', 'r') as messages:
        toast_message = messages.readline()
    st.set_page_config(page_title='The Constitution of India . QuizCrafter',page_icon='assets\\color.svg')    
    st.toast(toast_message)
    st.chat_input('Have a question about The Constitution of India? Ask here.')
    st.title(':open_book: The Constitution of India')
    st.markdown(':green[Learn all about the world\'s largest living document with the assistance of **AI**]')
    #st.divider()
    st.markdown(
        """
        The Constitution of India, adopted on January 26, 1950, is the supreme law of the country. It lays down the framework that defines the political principles, establishes the structure, procedures, powers, and duties of government institutions, and sets out fundamental rights, directive principles, and the duties of citizens. The Constitution of India is notable for several reasons:
        
        \n:one: **:red[Length and Detail:]** It is one of the lengthiest written constitutions in the world, containing 448 articles divided into 25 parts, 12 schedules, and 5 appendices.
        \n:two: **:red[Federal Structure with Unitary Features:]** It establishes a federal system of government, where power is divided between the central government and the states. However, it also incorporates strong unitary elements to maintain national unity and integrity.
        \n:three: **:red[Fundamental Rights:]** It guarantees fundamental rights to all citizens, including the right to equality, freedom of speech and expression, freedom of religion, and the right to constitutional remedies.
        \n:four: **:red[Directive Principles of State Policy:]** These principles guide the state in making laws and policies towards securing a just society. They are not enforceable by the courts but are fundamental in governance.
        \n:five: **:red[Parliamentary Democracy:]** India follows the parliamentary system of democracy, with a President as the head of state and a Prime Minister as the head of government. The President's role is largely ceremonial, while the Prime Minister is the chief executive.
        \n:six: **:red[Independent Judiciary:]** The Constitution establishes an independent judiciary headed by the Supreme Court, which is tasked with interpreting the Constitution and ensuring its enforcement.
        \n:seven: **:red[Amendment Procedure:]** The Constitution provides for its own amendment to adapt to changing circumstances. Amendments can be made through a special majority of Parliament, reflecting its flexibility.
        \n:eight: **:red[Secularism:]** India is a secular state according to its Constitution. It guarantees equal treatment of all religions by the state and ensures that the government does not favor any particular religion.

        \nThe Constitution of India reflects the aspirations and values of a diverse and pluralistic society, providing a framework for governance that has endured for over seven decades. It serves as a guiding light for the nation's progress, ensuring justice, liberty, equality, and fraternity for all its citizens.
        """
    )

if __name__ == '__main__':
    main()