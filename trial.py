import streamlit as st
import graphviz as graphviz
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
st.title('Graphviz')
graph = graphviz.Digraph()
graph.edge("A",'B')
graph.edge("B",'C')
graph.edge("C",'D')
graph.edge("E",'C')
graph.edge("F",'C')
st.graphviz_chart(graph)
