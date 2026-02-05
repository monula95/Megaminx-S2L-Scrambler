import streamlit as st
import mega

st.set_page_config(page_title="Megaminx S2L Scrambler")
st.title("Megaminx S2L Scrambler")

length = st.number_input("Scramble length", min_value=1, value=49)

# --- Custom large button using HTML ---
clicked = st.markdown(
    """
    <form action="#" method="POST">
        <button type="submit" style="
            font-size: 30px;
            padding: 20px 40px;
            border-radius: 12px;
            background-color:#4CAF50;
            color:white;
            font-weight:bold;
        ">Generate Scramble</button>
    </form>
    """,
    unsafe_allow_html=True
)

# --- Then generate scramble on click ---
if st.button("Generate Scramble (fallback)"):  # fallback if you want normal button
    scramble_str = mega.scramble(length)
    st.markdown(
        f"<div style='font-family:monospace; font-size:20px; white-space:pre'>{scramble_str}</div>", 
        unsafe_allow_html=True
    )
