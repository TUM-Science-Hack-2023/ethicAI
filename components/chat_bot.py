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
        
        def user_msg(content):
            # Possible avatar styles: https://github.com/AI-Yash/st-chat/issues/29#issuecomment-1547049574
            message(content, is_user=True, avatar_style="adventurer")
            
        def bot_msg(content):
            message(content, is_user=False, avatar_style="bottts")
        
        for msg in self.chat_history:
            if msg["role"] == "user":
                user_msg(msg["content"])
            else:
                user_msg(msg["content"])
        # 
        input_text = st.text_input("You: ", placeholder="Type here..." , key="chat_user_input")
        
        if input_text:
            with st.spinner('Running Text2Text. Please wait...'):
                self.step_chat(input_text)