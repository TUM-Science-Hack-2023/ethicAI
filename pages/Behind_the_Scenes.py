import streamlit as st


info_section = st.session_state["info_section"]

st.sidebar.header("EthicAI - Behind the Scenes")

info_section.render()