import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.colored_header import colored_header
from streamlit_extras.app_logo import add_logo


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
with st.sidebar:
    add_logo("media/logo.jpg", height=200)
    st.write("# Welcome to EthicAI! 👋")
    st.write("EthicAI *(eh·thuh·kl)* is the innovative, interactive problem solver for teachers, lectures, etc. at all levels with built-in risk assesment of the idea.")
    st.info("You may experience errors with certain features if many users access it at the same time.")
    
    # add_vertical_space(1)
    # st.markdown("""**Authors:**\n- [Altay Kacan](https://www.linkedin.com/in/altay-kaçan-0383131a3/)\n- [Dominika G.]()\n- [Razin Abdullah](https://www.linkedin.com/in/razin-abdullah/)\n- [Philipp Wulff](https://www.linkedin.com/in/philippwulff/)\n""")


# RENDER THE PAGE

add_vertical_space(3)
st.markdown("# Chat")
st.markdown("Have a chat with your personal AI ideation assistant to find a creative solution to your problem. If you like an idea, use the '➕' symbol to save it to the *Solution Notes*. Scroll down to view the *Solution Notes*.")

st.write("---")
chat_bot.render(solution_prototype.append_solution)
st.write("---")

add_vertical_space(3)

solution_prototype.render()
