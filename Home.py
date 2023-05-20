import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.colored_header import colored_header
from streamlit_extras.app_logo import add_logo


from components.chat_bot import ChatBot
from components.solution_prototype import SolutionPrototype
from components.info_section import InfoSection


def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(http://placekitten.com/200/200);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "My Company Name";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


# SETUP SESSION STATE
# Called after a page load/refresh

if "chat_bot" not in st.session_state:
    st.session_state["chat_bot"] = ChatBot()
if "solution_prototype" not in st.session_state:
    st.session_state["solution_prototype"] = SolutionPrototype()
if "info_section" not in st.session_state:
    st.session_state["info_section"] = InfoSection()
    
# SETUP FOR THIS RENDER

chat_bot = st.session_state["chat_bot"]
solution_prototype = st.session_state["solution_prototype"]

# SETUP PAGE INFO

st.set_page_config(
    page_title="EthicAI - Demo",
    page_icon=":robot:"
)
# add_logo("media/logo.jpeg", height=300)
add_logo()
st.sidebar.header("EthicAI")
with st.sidebar:
    add_vertical_space(3)
st.sidebar.write("# Welcome to EthicAI! 👋")


# RENDER THE PAGE

add_vertical_space(3)
st.markdown("# Chat")
st.markdown("Talk to the bot to find a solution to your problem.")

st.write("---")
chat_bot.render(solution_prototype.append_solution)
st.write("---")

add_vertical_space(3)
st.markdown("# Evaluation")
st.markdown("See how ethical your solution is and how it can be improved.")

solution_prototype.render()
