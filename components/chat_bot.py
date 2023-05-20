import streamlit as st
from streamlit_chat import message


DUMMY_CHAT_HISTORY =  [  
    {'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},    
    {'role':'user', 'content':'tell me a joke'},   
    {'role':'assistant', 'content':'Why did the chicken cross the road'},   
    {'role':'user', 'content':'I don\'t know'}  
]


class ChatBot:
    
    def __init__(self) -> None:
        # List of Dicts
        self.chat_history = DUMMY_CHAT_HISTORY
        
    def step_chat(self, user_input: str):
        self.chat_history.append({
            'role': 'user',
            'content': user_input
        })
        # do API call
    
    def render(self):
        
        for msg in self.chat_history:
            msg_role = msg["role"]
            msg_content = msg["content"]
            message(msg_content, is_user=msg_role=="user")
        
        # 
        input_text = st.text_input("You: ", placeholder="Type here..." , key="chat_user_input")
        
        if input_text:
            self.step_chat(input_text)