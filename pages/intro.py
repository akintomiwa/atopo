import streamlit as st 

def get_name():
    # Landing page. Get user handle
    st.title('Twitter Guru (GPT)')
    prompt = st.text_input('Type in your Twitter username')
    return prompt