import streamlit as st
import pandas as pd
url=st.text_input("url:")
ok=st.button("ok")
if ok:
    tables = pd.read_html(url)
    st.write(tables[1][1])
    st.write(tables[2])
    st.write(tables[3])
    st.write(tables[4])
    



