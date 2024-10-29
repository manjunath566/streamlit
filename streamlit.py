import streamlit as st
import ollama
st.write("hello")
user_prompt=st.text_area("hello")

def response(query):
    st.session_state.response=""
    response=ollama.generate("phi3",prompt=query,stream=True)
    for partial_resp in response:
        token=partial_resp["response"]
        st.session_state.response += token
        yield token
if st.button("Genarate"):
    st.write_stream(response(user_prompt))