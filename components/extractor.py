"""
This script has an extractor object that extracts the bulletpoints from the 
chat messages.
"""

import cohere   
import streamlit as st


class Extractor():
    def __init__(self) -> None:
        self.co = cohere.Client(st.secrets["COHERE_KEY"])

    
    def extract(self, text_to_extract):
        """
        This is supposed to have the functionality to
        take in individual messages from the chat and 
        summarize them as bullet points.
        """

        # Really hacky way to avoid errors with text shorter than 250 characters
        if len(text_to_extract) <= 250:
            text_to_extract += " " * (250 - len(text_to_extract))

        response = self.co.summarize(text=text_to_extract,
                                     length="medium",
                                     format="bullets",
                                     extractiveness="medium",
                                     temperature=0.1,
                                     additional_command="Focus on actionable steps or concrete descriptions. Keep the bulletpoints less than 100 characters"
        )

        response = response.summary # gets the string separated with "- ..." and "\n "

        response_list = response.split("\n")

        for i in range(len(response_list)):
            response_list[i] = response_list[i][2:]

        return response_list


