import time
import streamlit as st

with st.spinner("wait for it..."):
    time.sleep(5)
st.success("Done!")