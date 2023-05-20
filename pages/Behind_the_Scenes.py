import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.app_logo import add_logo
from components.info_section import InfoSection


if "info_section" not in st.session_state:
    st.session_state["info_section"] = InfoSection()
    
info_section = st.session_state["info_section"]

with st.sidebar:
    add_logo("media/logo.jpg", height=200)
    add_vertical_space(5)
    st.markdown("""Authors:\n- Altay Kacan\n- Dominika ...\n- Razin ....\n- Philipp Wulff\n""")


info_section.render()