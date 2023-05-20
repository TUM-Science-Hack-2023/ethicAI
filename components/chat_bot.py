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
        temperature=temperature, # this is the degree of randomness of the model's output
    )
        
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
        
        for msg in self.chat_history:
            msg_role = msg["role"]
            msg_content = msg["content"]
            message(msg_content, is_user=msg_role=="user")
        
        # 
        input_text = st.text_input("You: ", placeholder="Type here..." , key="chat_user_input")
        
        if input_text:
            self.step_chat(input_text)