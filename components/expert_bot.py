"""
This script contains the definition of the "expert" models that 
we are using for evaluating each of the ethical principles of 
using AI in education.

The main principles that we are considering are:
- Inclusive Growth, Sustainable Development, and Well-being
- Human-centred Values and Fairness
- Transparency and Explainability
- Robustness, Security, and Safety
- Accountability
- Child rights
- 
"""
import openai
import json
import os
import sys
import cohere 

sys.path.append("..")
from env import *

# Get API key
openai.api_key  = OPEN_AI_KEY

class ExpertBot():
    def __init__(self, expertise : str) -> None:
        # These are the specific prompts that will be used for the specific expert model
        self.prompts = {
        "inclusive":{"title": "Inclusive Growth, Sustainable Development, and Well-being",
                    "definition":"""
                    Stakeholders should proactively engage in responsible 
                    stewardship of trustworthy AI in pursuit of beneficial outcomes for
                    people and the planet, such as augmenting human capabilities and
                    enhancing creativity, advancing inclusion of underrepresented 
                    populations, reducing economic, social, gender and other inequalities,
                    and protecting natural environments, thus invigorating inclusive growth, 
                    sustainable development and well-being.
                    """,
                    "criteria":"""
                    Inclusive Growth:
                    Score of 1-3: Limited or no support for equal access, diverse learner needs, or overall growth and development.
                    Score of 4-6: Moderate support for some aspects of inclusive growth but lacking in others.
                    Score of 7-9: Strong support for equal access, diverse learner needs, and overall growth and development.
                    Score of 10: Exceptional support, going above and beyond to ensure inclusive growth in all aspects.

                    Sustainable Development:
                    Score of 1-3: Significant negative environmental impact with minimal or no efforts towards sustainability.
                    Score of 4-6: Some efforts towards sustainability but scope for improvement in reducing environmental impact.
                    Score of 7-9: Demonstrates commitment to sustainable practices and actively works to reduce environmental impact.
                    Score of 10: Exemplary efforts in sustainable development, contributing positively to the environment.

                    Well-being:
                    Score of 1-3: Little to no consideration for learner well-being, lacking resources or support.
                    Score of 4-6: Some attention to well-being but room for improvement in providing comprehensive support.
                    Score of 7-9: Prioritises learner well-being, offering resources, guidance, and support for mental and emotional health.
                    Score of 10: Exceptional commitment to learner well-being, providing comprehensive support and fostering a positive learning environment.
                    """,
                    "keys":["Inclusive Growth", "Sustainable Development", "Well-being"]
                    },
        "human":{"title": "Human-centred Values and Fairness",
                "definition":"""AI actors should respect the rule of law, human rights
                and democratic values, throughout the AI system lifecycle. These include 
                freedom, dignity and autonomy, privacy and data protection, 
                non-discrimination and equality, diversity, fairness, social justice, 
                and internationally recognized labor rights. To this end, AI actors 
                should implement mechanisms and safeguards, such as capacity for human 
                determination, that are appropriate to the context and consistent with 
                the state of art.
                """,
                "criteria":"""
                Human-centred Values:
                Score of 1-3: Demonstrates a lack of consideration for human rights, dignity, or equal treatment of learners.
                Score of 4-6: Shows some efforts in promoting human-centred values but has room for improvement.
                Score of 7-9: Prioritises human rights, dignity, and equal treatment, incorporating them into all aspects of the AI solution.
                Score of 10: Exemplary commitment to human-centred values, ensuring the rights and well-being of learners in all respects.
                
                Fairness:
                Score of 1-3: Exhibits significant biases, discrimination, or unfairness in decision-making processes.
                Score of 4-6: Some attempts to address biases and discrimination but with room for improvement.
                Score of 7-9: Demonstrates fairness in decision-making processes, actively works to minimise biases and discrimination.
                Score of 10: Exceptional fairness, ensuring unbiased and equitable treatment of all learners.
                """  
                },
        "transparency":{"title": "Transparency and Explainability",
                "definition":"""AI Actors should commit to transparency and responsible disclosure regarding AI systems.
                To this end, they should provide meaningful information, appropriate to the context, 
                and consistent with the state of art: i. to foster a general understanding of AI systems;
                ii. to make stakeholders aware of their interactions with AI systems, 
                including in the workplace; 
                iii. to enable those affected by an AI system to understand the outcome;and,
                iv. to enable those adversely affected by an AI system to challenge its outcome based on plain and easy-to-understand information on the factors, 
                and the logic that served as the basis for the prediction, recommendation or decision. 
                """,
                "criteria":"""
                Transparency:
                Score of 1-3: Provides little to no information about its functioning, decision-making processes, or underlying algorithms.
                Score of 4-6: Offers some level of transparency but lacks comprehensive explanations or insights into its operations.
                Score of 7-9: Demonstrates transparency by providing clear explanations of its functioning, decision-making processes, and underlying algorithms.
                Score of 10: Exemplary transparency, offering detailed and comprehensive insights into its operations.
                
                Explainability:
                Score of 1-3: Fails to provide any meaningful explanation of its decision-making processes, making it difficult to understand its actions.
                Score of 4-6: Provides limited explanations that may be insufficient to understand its decision-making processes.
                Score of 7-9: Offers meaningful explanations of its decision-making processes, enabling educators, students, and parents to understand its actions.
                Score of 10: Exceptional explainability, providing detailed and easily understandable explanations of its decision-making processes.
                """  
                },
        "robust":{"title": "Robustness, Security, and Safety",
                "definition":"""a) AI systems should be robust, 
                secure and safe throughout their entire lifecycle so that, 
                in conditions of normal use, foreseeable use or misuse, 
                or other adverse conditions, they function appropriately and do not pose unreasonable safety risk. 
                b) To this end, AI actors should ensure traceability, including in relation to datasets, 
                processes and decisions made during the AI system lifecycle, 
                to enable analysis of the AI systems outcomes and responses to inquiry,
                appropriate to the context and consistent with the state of art. 
                c) AI actors should, based on their roles, the context, and their ability to act,
                apply a systematic risk management approach to each phase of the AI system lifecycle on a continuous basis to address risks related to AI systems, 
                including privacy, digital security, safety and bias. 
                """,
                "criteria":"""
                Robustness:
                Score of 1-3: Demonstrates significant vulnerabilities, instability, or unreliability in its performance.
                Score of 4-6: Shows moderate robustness but has room for improvement in terms of stability and reliability.
                Score of 7-9: Demonstrates strong performance with high levels of stability and reliability in various scenarios.
                Score of 10: Exceptional robustness, with reliable and stable performance across a wide range of situations.

                Security:
                Score of 1-3: Exhibits major security flaws, data breaches, or inadequate protection of sensitive information.
                Score of 4-6: Demonstrates some security measures but may have vulnerabilities or areas that require improvement.
                Score of 7-9: Implements robust security measures to protect sensitive data and mitigate potential security risks.
                Score of 10: Exemplary security, with comprehensive measures to ensure the highest level of data protection and secu
                
                Safety:
                Score of 1-3: Poses significant safety risks or lacks proper measures to ensure physical or psychological safety of users.
                Score of 4-6: Demonstrates some safety measures but may have areas that require improvement to ensure user safety.
                Score of 7-9: Prioritises user safety by implementing measures to mitigate potential risks and ensure a safe environment.
                Score of 10: Exceptional safety measures, providing a secure and safe environment for users.
                """  
                },

        "accountable":{"title": "Accountability",
                "definition":"""AI actors should be accountable for the proper functioning of AI systems and for the respect
                of the above principles, based on their roles, the context, and consistent with the state of art.
                """,
                "criteria":"""
                Accountability: 
                Score of 1-3: Demonstrates a lack of clear lines of accountability and responsibility for system developers, educators, and administrators.
                Score of 4-6: Shows some efforts to establish accountability but may have areas that require improvement or clarification.
                Score of 7-9: Establishes clear lines of accountability, specifying roles and responsibilities for system developers, educators, and administrators.
                Score of 10: Exemplary accountability, with well-defined and comprehensive measures to ensure responsible use and oversight of the AI solution.
                """ 
                },

        "child":{"title": "Child Rights",
                "definition":"""The AI solution should prioritise and uphold the rights of children, ensuring their protection, privacy, and well-being.
                It should comply with child protection laws and regulations and incorporate age-appropriate content and interactions.
                """,
                "criteria":"""
                Child-Rights: 
                Score of 1-3: Demonstrates significant violations or neglect of child rights, such as privacy, safety, and protection from harmful content.
                Score of 4-6: Shows some efforts to protect child rights but may have areas that require improvement or further attention.
                Score of 7-9: Prioritises and safeguards child rights, ensuring privacy, safety, and protection from harmful content or exploitation.
                Score of 10: Exemplary commitment to upholding child rights, with comprehensive measures to protect and promote their well-being.
                """         
                }
        }

        assert expertise in self.prompts.keys(), "Provided expertise is not recognized! Please check available ones in components/expert_bot.py"
        self.expertise = expertise

        self.task_title = self.prompts[self.expertise]["title"]
        self.task = self.prompts[self.expertise]["definition"]
        self.scoring_scheme = self.prompts[self.expertise]["criteria"]

        self.prompt = None
        self.summary_prompt = None

        # Cohere object
        self.co = cohere.Client(COHERE_KEY)

    def get_evaluation(self, use_case, model="gpt-3.5-turbo"):
        """
        This function is supposed to receive the use case and 
        add it to the prompt of the system.

        The answer returned should be a JSON object (a python dictionary)
        """
        self.prompt = f"""
            Determine whether the given use case describing an use case of AI 
            delimited by three backticks is appropriate according to the 
            AI ethics principle of "{self.task_title}".

            The definition of this principle is: 
            "{self.task}"

            Evaluate the given use case based only on the given definition.
            Use a formal tone, give your answers in a concise manner.
            Make sure to point out any possible risks and explain why you think
            that is the case.


            Base your answers on the following scoring scheme:

            {self.scoring_scheme}

            The use case is:
            ```
            {use_case}
            ```

            Return your answer formatted as a JSON object with keys <criteria_name>
            each containing two subkeys <score> and <explanation_and_possible_risks>.
            """

        assert self.prompt is not None, f"Your prompt is empty in the expert system {self.expertise}!"

        try:
            messages = [{"role": "user", "content": self.prompt}]
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=0, # this is the degree of randomness of the model's output
            )

            # Returning the response as dictionary
            response_str = response.choices[0].message["content"]
            response_dict = json.loads(response_str)

        except Exception as e:
            response_dict = {"Please have some patience...":{
                "score":0, 
                "explanation_and_possible_risks":"""There are some rate limits 
                with model usage. You can wait a couple of minutes then try again.
                Ooooor, you can invest a couple of million dollars in us so we 
                can get a nice and shiny production key"""}}
        return  response_dict


    def get_short_summary(self, response_dict, model="gpt-3.5-turbo"):
        """
        This function expects to receive the response_dict the get_evaluation
        function returns and outputs a list containing a very brief summary of
        the given text
        """
        try:
            text_to_summarize = self.get_full_detail(response_dict)

            self.summary_prompt = f"""Extract the main ideas from the following text delimited by
            three backticks. Give your answer in no more than 50 characters.

            ```
            {text_to_summarize}
            ```
            """
            messages = [{"role": "user", "content": self.summary_prompt}]
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=0, # this is the degree of randomness of the model's output
            )

            response = response.choices[0].message["content"]
        except Exception as e:
            response = "Please have some patience, there are rate limits on how many calls we can make..."

        return response

    def get_short_summary_cohere(self, response_dict):
        """
        This is just a backup function that uses the Cohere API instead
        of the OpenAI one just to avoid rate limits.
        """
        try:
            text_to_summarize = self.get_full_detail(response_dict)

            response = self.co.summarize(text=text_to_summarize,
                                        length="short",
                                        format="paragraph",
                                        extractiveness="medium",
                                        additional_command="Limit your answer to one sentence with less than 50 characters.")
            
            response = response.summary # extracts the string
            
            # prompt = f"""Summarize the following text delimited by
            #  three backticks. Give your answer in no more than 50 characters.
            #  ```{text_to_summarize}```"""
            # response = self.co.generate(prompt=prompt,
            #                             model="command-nightly",
            #                             temperature=0)
        except Exception as e:
            response = "Please have some patience, there are rate limits on the calls we can make..."
        return response


    def get_avg_from_responsedict(self, response_dict):
        """
        Use this function to get the average score that the model returns
        after calling get_evaluation method of this class.

        The dictionary looks like this:

        ```
        {'Transparency': {'score': 4, 'explanation_and_possible_risks': 'The use 
        case offers some level of transparency by describing the use of cameras 
        to observe students and recognise violence and bullying in the classroom.
        However, it lacks comprehensive explanations of the decision-making 
        processes and underlying algorithms used for surveillance. This 
        lack of transparency could lead to concerns about privacy and
        potential misuse of the technology.'}, 
        'Explainability': {'score': 3, 'explanation_and_possible_risks': 'The use case fails
        to provide any meaningful explanation of its decision-making
        processes, making it difficult to understand its actions.
        This lack of explainability could lead to concerns about
        the accuracy and fairness of the surveillance system, 
        as well as potential biases in the data used to train 
        the AI algorithms.'}}
        ```
        """

        keys = list(response_dict.keys())

        total = 0

        for key in keys:
            response = response_dict[key]["score"]
            total += response 

        average = total / len(keys)

        return average

    def get_full_detail(self, response_dict):
        """
        This is just a nice-to-have function that can be used to get 
        a full text description from the response_dict
        """

        keys = list(response_dict.keys())
        response = ""
        for key in keys:
            response += key + ": " + response_dict[key]["explanation_and_possible_risks"] + "\n"

        return response



    


    


    
