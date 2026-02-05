import streamlit as st
import mega

st.set_page_config(page_title="Megaminx S2L Scrambler")

st.title("Megaminx S2L Scrambler")

length = st.number_input("Scramble length", min_value=1, value=49)

if st.button("Generate Scramble"):
    st.code(mega.scramble(length))
