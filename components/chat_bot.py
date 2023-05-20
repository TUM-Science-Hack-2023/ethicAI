import streamlit as st
from streamlit_chat import message


class ChatBot:
    
    def __init__(self) -> None:
        # List of Dicts
        self.chat_history = []
    
    def render(self):
        
        message("My message") 
        message("Hello bot!", is_user=True)     