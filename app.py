import streamlit as st
import mega

st.set_page_config(page_title="Megaminx S2L Scrambler")
st.title("Megaminx S2L Scrambler")

length = st.number_input("Scramble length", min_value=1, value=49)

st.markdown(
    """
    <style>
    div.stButton > button {
        padding: 25px 50px;   /* big button area */
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Then generate scramble on click ---
if st.button("Generate Scramble"):  # fallback if you want normal button
    scramble_str = mega.scramble(length)
    st.markdown(
        f"<div style='font-family:monospace; font-size:20px; white-space:pre'>{scramble_str}</div>", 
        unsafe_allow_html=True
    )
