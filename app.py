import streamlit as st
import mega

st.set_page_config(page_title="Megaminx S2L Scrambler")
st.title("Megaminx S2L Scrambler")

length = st.number_input("Scramble length", min_value=1, value=49)

if st.button("Generate Scramble"):
    scramble_str = mega.scramble(length)
    
    st.markdown(
        f"<div style='font-family:monospace; font-size:20px; white-space:pre'>{scramble_str}</div>", 
        unsafe_allow_html=True
    )
