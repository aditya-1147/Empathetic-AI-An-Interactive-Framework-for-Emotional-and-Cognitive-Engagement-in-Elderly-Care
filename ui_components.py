# ui/ui_components.py

import streamlit as st

def display_header(title, subtitle):
    st.markdown(
        f"""
        <h1 style='text-align: center;'>{title}</h1>
        <p style='text-align: center; font-size: 18px;'>{subtitle}</p>
        <hr>
        """,
        unsafe_allow_html=True
    )


def user_input_box():
    return st.text_area(
        "Type your message here:",
        height=120,
        placeholder="You can talk to me about anything…",
    )


def send_button():
    return st.button("Send", use_container_width=True)
