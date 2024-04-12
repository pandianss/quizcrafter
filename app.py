import streamlit as st
import pandas as pd
import numpy as np
st.title('Learning - Zoom Mode', anchor='Apress')
st.header('This is a Header', anchor="Apress")
st.subheader('This is a subheader')
st.caption('This is a caption')
st.text('This is plain text')
st.latex(r'''cos2\theta=1-2sin^2\theta''')
code = '''def hello():
print('Satish')'''
st.code(code, language='python')
df = pd.DataFrame(np.random.randn(30,10),columns=('col_no %d' % i for i in range(10)))
st.dataframe(df)