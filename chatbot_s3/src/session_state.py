import streamlit as st 
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'
    
def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)

with st.form(key='my_form'):
    slider_input = st.slider('my slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox("yes or no", key="my_checkbox")
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)