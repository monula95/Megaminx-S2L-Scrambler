import streamlit as st
import mega

st.set_page_config(page_title="Megaminx S2L Scrambler")
st.title("Megaminx S2L Scrambler")

length = st.number_input("Scramble length", min_value=1, value=49)

st.markdown(
    """
    <style>
    /* Make all buttons bigger */
    div.stButton > button {
        font-size: 20px;       /* Bigger text */
        padding: 30px 50px;    /* More padding top/bottom and left/right */
        border-radius: 10px;   /* Rounded corners, optional */
    }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("Generate Scramble"):
    scramble_str = mega.scramble(length)
    
    st.markdown(
        f"<div style='font-family:monospace; font-size:30px; white-space:pre'>{scramble_str}</div>", 
        unsafe_allow_html=True
    )
