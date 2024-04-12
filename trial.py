import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

data = np.random.randn(5,2)
df = pd.DataFrame(data,columns=['a','b'])
chart = alt.Chart(df).mark_bar().encode(x='a',y='b',tooltip=['a','b'])

st.write(df)
st.write(chart)