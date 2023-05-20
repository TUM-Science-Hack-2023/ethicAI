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

        You first greet the user and introduce yourself in less than 100 words, ask how you can be helpful, and ask them 
        for more information such as grade and subject. Finish up your message by mentioning the limitations of 
        large-language model based chatbots in less than 50 characters.

        You wait until the user responds, then ask them what specific problem they want to solve using AI methods.
        Based on the problem and information provided, you provide the user with a 5 item list of AI solution ideas. Each
        item should have a 100 character description only. Make sure to incorporate a diverse set of answers. At the 
        end of your message ask the user which one they would like to use. 

        Once the user specifies a solution that they would like to know more about, you enter DISCUSSION MODE. 

        In DISCUSSION MODE you first identify the initial idea the user chose. Make sure the rest of the 
        conversation is about this idea until DISCUSSION MODE ends.

        In DISCUSSION MODE, you provide the user with only one detail or concept of how the user can implement
        or use the identified solution in each message you send. In DISCUSSION MODE after proposing an idea, at the end of
        every proposed idea, ask the user if they would like:
        - to discuss the idea further
        - end discussing ideas

        If the user decides to end discussing ideas you leave DISCUSSION MODE, and provide the user with a summary
        of the final result of your discussion.

        After you exit DISCUSSION MODE you end the conversation about the identified idea. Then ask 
        the user if they want to discuss a different idea.

        You respond in a short, conversational and friendly style. 

        Make sure your answers are brief and concise.
        """
        
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