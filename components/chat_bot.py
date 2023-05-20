import streamlit as st
import openai
import random
from streamlit_chat import message


DUMMY_CHAT_HISTORY =  [  
    {'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},    
    {'role':'user', 'content':'tell me a joke'},   
    {'role':'assistant', 'content':'Why did the chicken cross the road'},   
    {'role':'user', 'content':'I don\'t know'}  
]


class ChatBot: 
    def __init__(self) -> None:
        """
        This is the main class for interacting with the chatbot from the front-end.
        The chat history is saved as a list of dictionaries, e.g.:

        ```
        messages =  [  
        {'role':'system', 'content':'You are an assistant that speaks like a Pirate.'},    
        {'role':'user', 'content':'tell me a joke'},   
        {'role':'assistant', 'content':'Why did the chicken cross the road'},   
        {'role':'user', 'content':'I don\'t know'}  ]
        ```

        There are three roles for the openAI chatbot API, 'system', 'user', and
        'assistant'.

        """
        self.system_prompt = """ """
        
        # List of Dicts
        self.chat_history = []

        # Init chat history with system prompt
        self.chat_history.append({"role":"system", "content":self.system_prompt})

    def get_completion_from_history(self, messages, model="gpt-3.5-turbo", temperature=0):
        response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, )# this is the degree of randomness of the model's output

        return response.choices[0].message["content"]
        
    def get_completion_from_history_dummy(self, messages, model=None, temperature=0):
        answers = ["How does that make you feel?", "Hmmmm", "Can you tell me more about that?", "bruh", "LOL"]
        response = random.choice(answers)

        return response


        
    def step_chat(self, user_input: str):
        self.chat_history.append({
            'role': 'user',
            'content': user_input
        })
        # do API call
        # response = self.get_completion_from_history(self.chat_history)

        # dummy response
        response = self.get_completion_from_history_dummy(self.chat_history)

        self.chat_history.append({"role":"assistant", "content": response})
    
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