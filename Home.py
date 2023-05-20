import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.colored_header import colored_header


from components.chat_bot import ChatBot
from components.solution_prototype import SolutionPrototype



# SETUP SESSION STATE
# Called after a page load/refresh

if "chat_bot" not in st.session_state:
    st.session_state["chat_bot"] = ChatBot()
if "solution_prototype" not in st.session_state:
    st.session_state["solution_prototype"] = SolutionPrototype()

# SETUP FOR THIS RENDER

chat_bot = st.session_state["chat_bot"]
solution_prototype = st.session_state["solution_prototype"]

# SETUP PAGE INFO

st.set_page_config(
    page_title="EthicAI - Demo",
    page_icon=":robot:"
)
st.sidebar.header("EthicAI")
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


