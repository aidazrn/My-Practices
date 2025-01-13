import streamlit as st
from file_1 import shop  

st.title("جست و جوی محصول...")
product_name = st.text_input("نام محصول موردنظر را وارد کنید: ")

if st.button("Search"):
    if product_name.strip():
        st.info(f"جست و جو برای '{product_name}'...")
        try:
            shop(product_name)
            st.success(f"جست و جو برای '{product_name}' تمام شد!")
        except Exception as e:
            st.error(f"ارور: {e}")
    else:
        st.warning("نام یک محصول را وارد کنید.")
