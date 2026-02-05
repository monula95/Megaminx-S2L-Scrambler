import streamlit as st
import mega

st.set_page_config(page_title="Megaminx S2L Scrambler")
st.title("Megaminx S2L Scrambler")

length = st.number_input("Scramble length", min_value=1, value=49)

if st.button("Generate Scramble"):
    scramble_str = mega.scramble(length)
    
    # Replace newlines with <br> so HTML renders them
    scramble_html = scramble_str.replace("\n", "<br>")
    
    st.markdown(f"<pre style='font-family: monospace; font-size:16px'>{scramble_html}</pre>", unsafe_allow_html=True)
