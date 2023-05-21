import streamlit as st
import openai
import sys
import random
from streamlit_chat import message

DUMMY_CHAT_HISTORY =  [  
    {'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},    
    {'role':'user', 'content':'tell me a joke'},   
    {'role':'assistant', 'content':'Why did the chicken cross the road'},   
    {'role':'user', 'content':'I don\'t know'}  
]
sys.path.append("..")
from env import *
openai.api_key  = OPEN_AI_KEY

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
        self.system_prompt = """
        You are an AI ideation assistant, an automated service that provides assistance and guidance to teachers 
        to come up with AI use-cases that they can use in the classroom to solve certain problems they might have.

        You have two modes OPEN MODE and DISCUSSION MODE. You start in OPEN MODE.

        You first greet the user and introduce yourself in less than 100 words, ask how you can be helpful, and ask them 
        for more information such as grade and subject. Finish up your message by additionally mentioning the limitations of 
        large-language model based chatbots in less than 50 characters.

        You wait until the user responds, then ask them what specific problem they want to solve using AI methods.

        In OPEN MODE, you provide a list of 5 ideas of how the teacher can apply AI solutions effectively
        to his or her situation. Each item should have a 100 character description only. Make sure to incorporate a diverse set of answers. At the 
        end of your message ask the user which one they would like to use. 

        Once the user specifies a solution that they would like to know more about, you enter DISCUSSION MODE. 

        In DISCUSSION MODE you first identify the initial idea the user chose. Make sure the rest of the 
        conversation is about this idea until DISCUSSION MODE ends.

        In DISCUSSION MODE, you provide the user with only one detail or concept of how the user can implement
        or use the identified solution in each message you send. In DISCUSSION MODE after proposing a detail or concept, you
        ask the user if they would like:
        - to discuss the idea further
        - to move on to a new idea
        - to end discussing ideas

        If the user decides to end discussing ideas you leave DISCUSSION MODE, and provide the user with a summary
        of the final result of your discussion. Remind the user that large language model based chatbots have limitations
        and briefly mention what the user should be aware of.

        You respond in a short, conversational and friendly style. 

        Make sure your answers are brief and concise.
        """
        
        # List of Dicts
        self.chat_history = []

        # Init chat history with system prompt
        self.chat_history.append({"role":"system", "content":self.system_prompt})
        self.chat_history.append({
            "role": "assistant", 
            "content": "Hello! I'm an AI ideation assistant here to help you come up with AI use-cases for your classroom. What grade and subject do you teach? How can I assist you today? Please note that large language model based chatbots have limitations."
        })

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
        response = "Sorry, too many users access my service right now and there is a rate limit for my API."
        try:
            response = self.get_completion_from_history(self.chat_history)
        except Exception as e:
            st.sidebar.error(f"Retrieving the chatbot's response failed. Please try again.")
            # st.sidebar.error(f"Retrieving the chatbot's response failed with error: {e}")

        # dummy response
        # response = self.get_completion_from_history_dummy(self.chat_history)

        self.chat_history.append({"role":"assistant", "content": response})
    
    def render(self, send_message_text_func=None):
        
        def user_msg(content, num):
            # Possible avatar styles: https://github.com/AI-Yash/st-chat/issues/29#issuecomment-1547049574
            message(content, is_user=True, avatar_style="avataaars", key=f"user_msg_{num}")
            
        def bot_msg(content, num):
            col1, col2 = st.columns([1, 12])
            with col1:
                def on_click_func():
                    send_message_text_func(content)
                st.button("➕", help="Add this to your solution!", on_click=on_click_func if send_message_text_func else None, key=f"bot_msg_button_{num}")
            with col2: 
                message(content, is_user=False, avatar_style="bottts", key=f"bot_msg_{num}")
            
        for i, msg in enumerate(self.chat_history):
            if msg["role"] == "user":
                user_msg(msg["content"], i)
            elif msg["role"] == "assistant":
                bot_msg(msg["content"], i)
                
        
        if not "chat_user_input" in st.session_state:
            st.session_state["chat_user_input"] = ""
            
        def process_input(): 
            self.step_chat(st.session_state["chat_user_input"])
            st.session_state["chat_user_input"] = ""
        
        st.text_input("You:", placeholder="Type your response here...", on_change=process_input, key="chat_user_input", label_visibility="collapsed")
    
            