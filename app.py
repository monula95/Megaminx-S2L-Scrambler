import streamlit as st
import s2l

# --- Page config ---
st.set_page_config(page_title="Megaminx Scrambler")
st.title("Megaminx Scrambler")


# --- Dropdown to choose scrambler ---
scrambler_type = st.selectbox(
    "Choose Scrambler",
    ["S2L Scrambler", "Full Scrambler"]
)

# --- CSS for centered, large buttons ---
st.markdown(
    """
    <style>
    div.stButton {
        display: flex;
        justify-content: center;
    }
    div.stButton > button {
        padding: 25px 50px;
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Define S2L scrambler page ---
def s2l_page():
    length = st.number_input("Scramble length", min_value=1, value=48)

    # Center the button using columns
    _, col2, _ = st.columns([1,2,1])
    if col2.button("Generate S2L Scramble"):
        scramble_str = s2l.scramble(length)
        st.markdown(
            f"<div style='font-family:monospace; font-size:20px; white-space:pre'>{scramble_str}</div>",
            unsafe_allow_html=True
        )

# --- Define full scrambler page ---
def full_scrambler_page():
    st.write("Full scrambler coming soon...")

# --- Render the page based on selection ---
if scrambler_type == "S2L Scrambler":
    s2l_page()
else:
    full_scrambler_page()
