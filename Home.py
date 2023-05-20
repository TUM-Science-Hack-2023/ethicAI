import streamlit as st

from components.chat_bot import ChatBot
from components.solution_prototype import SolutionPrototype



# SETUP SESSION STATE
# Called after a page load/refresh

if "chat_bot" not in st.session_state:
    st.session_state["chat_bot"] = ChatBot()

# SETUP FOR THIS RENDER

chat_bot = st.session_state["chat_bot"]

# SETUP PAGE INFO

st.set_page_config(
    page_title="EthicAI - Demo",
    page_icon=":robot:"
)

# RENDER THE PAGE

st.write("# Welcome to EthicAI! 👋")


chat_bot.render()