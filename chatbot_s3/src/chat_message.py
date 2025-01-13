import streamlit as st
import numpy as np

with st.chat_message("ai"):
    st.write("Hello :wave:")
    st.line_chart(np.random.rand(30, 0))