import streamlit as st

from components.chat_bot import ChatBot
from components.solution_prototype import SolutionPrototype



st.set_page_config(
    page_title="EthicAI - Demo",
    page_icon=":robot:"
)

st.write("# Welcome to EthicAI! 👋")


chat_bot = ChatBot()


chat_bot.render()