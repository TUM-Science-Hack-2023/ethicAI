import streamlit as st


class InfoSection:
    
    def __init__(self) -> None:
        pass
    
    
    def render(self):
        st.header(body="Behind the scenes!") 
        st.markdown("""This tool uses custom made system prompts based on G20 Trustworthy guidelines to evaluate the AI solutions. System prompts are instructions or queries provided to an AI model to guide its responses and generate coherent and relevant output. The following are the scoring criteria that are used for evaluation, which we showcase to add transparency and inform the users. You can learn more about the trustworthy AI guidelines from [here](https://www.oecd.org/education/trustworthy-artificial-intelligence-in-education.pdf).""")
        st.markdown('##')
        st.markdown("<h4 style='text-align: left'>Click one of the following boxes to learn how your AI solutions get evaluated! </h4>", unsafe_allow_html=True)
        with st.expander("ChatBots and Large Language Models"):
              st.write("""This tool is built using instruction-tuned large language models. They have been
              pretrained on a huge amount of data to be able to understand grammar and semantics of languages. 
              They then get feedback to answer queries from humans in a preferable way. Even though these
              systems are extremely powerful and useful, they have some weaknesses. You should always
              fact-check and think about whether what the model outputs makes sense.
              \n You can learn more about Large Language Models using from [the OpenAI page](https://openai.com/blog/chatgpt), [Wikipedia](https://en.wikipedia.org/wiki/Large_language_model). 
              \n Furthermore, these chatbots are initialized with what is called a "system prompt". It is simply
              the message that the developers give to the model to prime it and give instructions on 
              how it should interact with the user. For transparency, here's the system
              prompt we used to instruct our AI ideation assistant to be helpful to you 
              as much as possible:



                ```
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
    ```""")
        with st.expander("Inclusive Growth, Sustainable Development, and Well-being"):
            st.write("""Stakeholders should proactively engage in responsible 
                        stewardship of trustworthy AI in pursuit of beneficial outcomes for
                        people and the planet, such as augmenting human capabilities and
                        enhancing creativity, advancing inclusion of underrepresented 
                        populations, reducing economic, social, gender and other inequalities,
                        and protecting natural environments, thus invigorating inclusive growth, 
                        sustainable development and well-being. 

                    Criteria:
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
                    Score of 10: Exceptional commitment to learner well-being, providing comprehensive support and fostering a positive learning environment.""")

        with st.expander("Human-centred Values and Fairness"):
                st.write("""AI actors should respect the rule of law, human rights
                    and democratic values, throughout the AI system lifecycle. These include 
                    freedom, dignity and autonomy, privacy and data protection, 
                    non-discrimination and equality, diversity, fairness, social justice, 
                    and internationally recognized labor rights. To this end, AI actors 
                    should implement mechanisms and safeguards, such as capacity for human 
                    determination, that are appropriate to the context and consistent with 
                    the state of art.

                Criteria:
                Human-centred Values:
                Score of 1-3: Demonstrates a lack of consideration for human rights, dignity, or equal treatment of learners.
                Score of 4-6: Shows some efforts in promoting human-centred values but has room for improvement.
                Score of 7-9: Prioritises human rights, dignity, and equal treatment, incorporating them into all aspects of the AI solution.
                Score of 10: Exemplary commitment to human-centred values, ensuring the rights and well-being of learners in all respects.

                Fairness:
                Score of 1-3: Exhibits significant biases, discrimination, or unfairness in decision-making processes.
                Score of 4-6: Some attempts to address biases and discrimination but with room for improvement.
                Score of 7-9: Demonstrates fairness in decision-making processes, actively works to minimise biases and discrimination.
                Score of 10: Exceptional fairness, ensuring unbiased and equitable treatment of all learners.""")

        with st.expander("Transparency and Explainability"):
                st.write("""AI Actors should commit to transparency and responsible disclosure regarding AI systems.
                    To this end, they should provide meaningful information, appropriate to the context, 
                    and consistent with the state of art: 
                    i. to foster a general understanding of AI systems;
                    ii. to make stakeholders aware of their interactions with AI systems, 
                    including in the workplace; 
                    iii. to enable those affected by an AI system to understand the outcome;and,
                    iv. to enable those adversely affected by an AI system to challenge its outcome based on plain and easy-to-understand information on the factors, 
                    and the logic that served as the basis for the prediction, recommendation or decision. 

                Criteria:     
                Transparency:
                Score of 1-3: Provides little to no information about its functioning, decision-making processes, or underlying algorithms.
                Score of 4-6: Offers some level of transparency but lacks comprehensive explanations or insights into its operations.
                Score of 7-9: Demonstrates transparency by providing clear explanations of its functioning, decision-making processes, and underlying algorithms.
                Score of 10: Exemplary transparency, offering detailed and comprehensive insights into its operations.

                Explainability:
                Score of 1-3: Fails to provide any meaningful explanation of its decision-making processes, making it difficult to understand its actions.
                Score of 4-6: Provides limited explanations that may be insufficient to understand its decision-making processes.
                Score of 7-9: Offers meaningful explanations of its decision-making processes, enabling educators, students, and parents to understand its actions.
                Score of 10: Exceptional explainability, providing detailed and easily understandable explanations of its decisions""")

        with st.expander("Robustness, Security, and Safety"):
                st.write("""AI systems should be robust, 
                    secure and safe throughout their entire lifecycle so that, 
                    in conditions of normal use, foreseeable use or misuse, 
                    or other adverse conditions, they function appropriately and do not pose unreasonable safety risk.
                    To this end, AI actors should ensure traceability, including in relation to datasets, 
                    processes and decisions made during the AI system lifecycle, 
                    to enable analysis of the AI systems outcomes and responses to inquiry,
                    appropriate to the context and consistent with the state of art. 
                    AI actors should, based on their roles, the context, and their ability to act,
                    apply a systematic risk management approach to each phase of the AI system lifecycle on a continuous basis to address risks related to AI systems, 
                    including privacy, digital security, safety and bias. 

                Criteria:     
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
                Score of 10: Exceptional safety measures, providing a secure and safe environment for users.""")


        with st.expander("Accountability"):
                st.write(""" AI actors should be accountable for the proper functioning of AI systems and for the respect
                    of the above principles, based on their roles, the context, and consistent with the state of art.

                Criteria:     
                Accountability: 
                Score of 1-3: Demonstrates a lack of clear lines of accountability and responsibility for system developers, educators, and administrators.
                Score of 4-6: Shows some efforts to establish accountability but may have areas that require improvement or clarification.
                Score of 7-9: Establishes clear lines of accountability, specifying roles and responsibilities for system developers, educators, and administrators.
                Score of 10: Exemplary accountability, with well-defined and comprehensive measures to ensure responsible use and oversight of the AI solution.""")

        with st.expander("Child Rights"):
                st.write(""" The AI solution should prioritise and uphold the rights of children, ensuring their protection, privacy, and well-being.
                It should comply with child protection laws and regulations and incorporate age-appropriate content and interactions.

                Criteria:     
                Child-Rights: 
                Score of 1-3: Demonstrates significant violations or neglect of child rights, such as privacy, safety, and protection from harmful content.
                Score of 4-6: Shows some efforts to protect child rights but may have areas that require improvement or further attention.
                Score of 7-9: Prioritises and safeguards child rights, ensuring privacy, safety, and protection from harmful content or exploitation.
                Score of 10: Exemplary commitment to upholding child rights, with comprehensive measures to protect and promote their well-being.""")
        
        
                    
        
