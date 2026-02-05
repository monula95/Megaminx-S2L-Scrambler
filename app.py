import streamlit as st
import mega

st.set_page_config(page_title="Megaminx S2L Scrambler")
st.title("Megaminx S2L Scrambler")

length = st.number_input("Scramble length", min_value=1, value=49)

# --- Create 3 columns: left, center, right ---
col1, col2, col3 = st.columns([1,2,1])  # middle column is wider

# Place button in the middle column
if col2.button("Generate Scramble"):
    scramble_str = mega.scramble(length)
    st.markdown(
        f"<div style='font-family:monospace; font-size:20px; white-space:pre'>{scramble_str}</div>",
        unsafe_allow_html=True
    )
