# 실행방법 : "streamlit run app.py" or "python3 -m streamlit run app.py"
import streamlit as st
import pandas as pd

view = [100, 150, 30]
st.write('# Youtube view')
st.write('## raw')
view
st.write('## bar chart')
st.bar_chart(view)

sview = pd.Series(view)
sview