import streamlit as st
from streamlit_extras.chart_container import chart_container
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space

from components.expert_bot import ExpertBot
from components.extractor import Extractor

import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import copy


class SolutionPrototype:
    
    def __init__(self) -> None:
        self.solution_name = ""
        self.solution_bullet_points = []
        self.solution_bullet_points_to_pop = []
        # 6 ethical dimensions
        self.ethics_dimensions = {
            "child": {
                "expert_bot": ExpertBot("child"),
                "score": 0,
                "risk": "",
                "risk_short": "",
                "display_name": "Child rights",
            },
            "human": {
                "expert_bot": ExpertBot("human"),
                "score": 0,
                "risk": "",
                "risk_short": "",
                "display_name": "Human-centred Values & Fairness",
            },
            "transparency": {
                "expert_bot": ExpertBot("transparency"),
                "score": 0,
                "risk": "",
                "risk_short": "",
                "display_name": "Transparency & Explainability",
            },
            "robust": {
                "expert_bot": ExpertBot("robust"),
                "score": 0,
                "risk": "",
                "risk_short": "",
                "display_name": "Robustness & Safety", # "Robustness, Security, and Safety"
            },
            "accountable": {
                "expert_bot": ExpertBot("accountable"),
                "score": 0,
                "risk": "",
                "risk_short": "",
                "display_name": "Accountability",
            },
            "inclusive": {
                "expert_bot": ExpertBot("inclusive"),
                "score": 0,
                "risk": "",
                "risk_short": "",
                "display_name": "Inclusive Growth & Sustainable Devpt.", # "Inclusive Growth, Sustainable Development, and Well-being"
            },
        }
        
        self.solution_text_extractor = Extractor()
        
        if not "solution_custom_text_input" in st.session_state:
            st.session_state["solution_custom_text_input"] = ""
        
        
    def append_solution(self, solution):
        solutions_list = self.solution_text_extractor.extract(solution)
        for el in solutions_list:
            self.solution_bullet_points.append(el)
        
    def concat_bullet_points(self):
        """Output should be e.g.
        - Using cameras in classroom to observe students
        - Recognise violence and bullying in the classroom
        - Surveillance of classroom settings
        """
        free_text = ["- " + _ for _ in self.solution_bullet_points]
        free_text = "\n".join(free_text)
        return free_text
        
    def update_ethics_radar(self):
        
        free_text = self.concat_bullet_points()
        cnt = 0
        successful_evals = 0
        for dim, dim_dict in self.ethics_dimensions.items():
            print("dim", dim)
            try:
                response_dict = dim_dict["expert_bot"].get_evaluation(free_text)
                self.ethics_dimensions[dim]["score"] = dim_dict["expert_bot"].get_avg_from_responsedict(response_dict)
                self.ethics_dimensions[dim]["risk"] = dim_dict["expert_bot"].get_full_detail(response_dict)
                self.ethics_dimensions[dim]["risk_short"] = dim_dict["expert_bot"].get_short_summary(response_dict)
            except Exception as e:
                # st.sidebar.error(f"Evaluation retrieval from expert:{dim} failed with error: {e}")
                st.sidebar.error(f"Evaluation retrieval from the {dim} expoert failed with error. Please try again.")
                continue
            
            successful_evals += 1
            cnt += 1
            if cnt == 2:
                break
        if successful_evals == len(self.ethics_dimensions):
            st.sidebar.success("Calculated all ethics scores!")
        elif successful_evals > 0:
            st.sidebar.success("Calculated some ethics scores!")
    
        
    def make_ethics_radar(self):
        """6 ethical dimensions."""
        data = go.Scatterpolar(
            r=[v["score"] for k, v in self.ethics_dimensions.items()],
            theta=[v["display_name"] for k, v in self.ethics_dimensions.items()],
            fill='toself'
        )

        fig = go.Figure(data=data)
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 10]),),
            showlegend=False,
            font=dict(size=18),
        )
        return fig
    
    def render(self):
        
        st.markdown("# Solution Notes")
        st.markdown("These notes contain the key details about your idea. Add details manually or by clicking the '➕' symbols in the chat.")
        
        # Pop buttons that were clicked in the last iteration
        for idx in self.solution_bullet_points_to_pop:
            self.solution_bullet_points.pop(idx)
        self.solution_bullet_points_to_pop = []
        
        for i, sbp in enumerate(self.solution_bullet_points):
            col1, col2, col3 = st.columns([10, 1, 1])
            with col1:
                st.text_input("No-show", value=sbp, disabled=True, label_visibility="collapsed", key=f"solution_text_field_{i}")
            with col2:
                st.button("🖋️", key=f"solution_edit_button_{i}")
            with col3:
                if st.button("❌", key=f"solution_del_button_{i}"):
                    self.solution_bullet_points_to_pop.append(i)

        # Add a custom input button
        def on_change_func():
            text = st.session_state["solution_custom_text_input"]
            if text:
                self.solution_bullet_points.append(text)
            st.session_state["solution_custom_text_input"] = ""
            
        st.text_input(
            "Custom input", 
            placeholder="Add a detail to your idea here...", 
            on_change=on_change_func, 
            label_visibility="collapsed",
            key="solution_custom_text_input"
        )
        
        # EVAL BUTTON
        if self.solution_bullet_points:
            st.button("Evaluate Ethics", on_click=self.update_ethics_radar, key=f"solution_eval_ethics_button")
        
        add_vertical_space(3)
        st.markdown("# Evaluation")
        st.markdown("Learn about the risks of your idea and its trustworthiness. Get insights about how to improve your idea.")
        
        colored_header(
            label="Risk Dimensions",
            description="Rate your idea within 6 guidelines of trustworthiness. You can learn more about these guidelines in the 'Behind the Scenes' page.",
            color_name="green-70",
        )   
        # RENDER THE PLOTLY RADAR FIGURE
        st.plotly_chart(self.make_ethics_radar(), use_container_width=True)

        colored_header(
            label="Identified Risks",
            description="Get detailed insights into the scores and specific risks.",
            color_name="green-70",
        )        
        for ethics_dim, risk_dict in self.ethics_dimensions.items():
            st.markdown(f"**{risk_dict['display_name']}:**")
            with st.expander(risk_dict['risk_short']):
                st.write(risk_dict["risk"])