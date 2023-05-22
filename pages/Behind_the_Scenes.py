import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.app_logo import add_logo
from components.info_section import InfoSection


if "info_section" not in st.session_state:
    st.session_state["info_section"] = InfoSection()
    
info_section = st.session_state["info_section"]

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

with st.sidebar:
    add_logo("media/logo.jpg", height=300)
    # add_vertical_space(14)
    st.markdown("""**Authors:**\n- [Altay Kacan](https://www.linkedin.com/in/altay-kaçan-0383131a3/)\n- [Dominika Golebiewska](https://www.linkedin.com/in/dominika-g-230056181/)\n- [Razin Abdullah](https://www.linkedin.com/in/razin-abdullah/)\n- [Philipp Wulff](https://www.linkedin.com/in/philippwulff/)\n""")


info_section.render()