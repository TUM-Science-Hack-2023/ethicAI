import streamlit as st
from streamlit_extras.chart_container import chart_container
from streamlit_extras.colored_header import colored_header
from components.expert_bot import ExpertBot

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
            "inclusive": {
                "expert_bot": ExpertBot("inclusive"),
                "score": 0,
                "risk": "",
                "risk_short": "",
                "display_name": "Inclusive Growth, Sustainable Development, and Well-being",
            },
            "human": {
                "expert_bot": ExpertBot("human"),
                "score": 0,
                "risk": "",
                "risk_short": "",
                "display_name": "Human-centred Values and Fairness",
            },
            "transparency": {
                "expert_bot": ExpertBot("transparency"),
                "score": 0,
                "risk": "",
                "risk_short": "",
                "display_name": "Transparency and Explainability",
            },
            "robust": {
                "expert_bot": ExpertBot("robust"),
                "score": 0,
                "risk": "",
                "risk_short": "",
                "display_name": "Robustness, Security, and Safety",
            },
            "accountable": {
                "expert_bot": ExpertBot("accountable"),
                "score": 0,
                "risk": "",
                "risk_short": "",
                "display_name": "Accountability",
            },
            "child": {
                "expert_bot": ExpertBot("child"),
                "score": 0,
                "risk": "",
                "risk_short": "",
                "display_name": "Child rights",
            },
        }
        
        if not "solution_custom_text_input" in st.session_state:
            st.session_state["solution_custom_text_input"] = ""
        
        
    def append_solution(self, solution):
        self.solution_bullet_points.append(solution)
        
    def concat_bullet_points(self):
        free_text = ["- " + _ for _ in self.solution_bullet_points]
        free_text = "\n".join(free_text)
        return free_text
        
    def update_ethics_radar(self):
        free_text = self.concat_bullet_points()
        for dim, dim_dict in self.ethics_dimensions:
            
            response_dict = dim_dict["expert_bot"].get_evaluation(free_text)
            self.ethics_dimensions[dim]["score"] = dim_dict["expert_bot"].get_avg_from_responsedict(response_dict)
            self.ethics_dimensions[dim]["risk"] = dim_dict["expert_bot"].get_full_detail(response_dict)
            self.ethics_dimensions[dim]["risk_short"] = dim_dict["expert_bot"].get_short_summary(response_dict)
        
    def make_ethics_radar(self):
        """6 ethical dimensions."""
        data = go.Scatterpolar(
            r=[v["score"] for k, v in self.ethics_dimensions.items()],
            theta=[v["display_name"] for k, v in self.ethics_dimensions.items()],
            fill='toself'
        )

        fig = go.Figure(data=data)
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True),),
            showlegend=False,
            font=dict(size=18),
            

        )
        return fig
    
    def render(self):
        
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
        
        colored_header(
            label="Risk Dimensions",
            description="See how ethical your idea is within the 6 dimensions of ethics in AI.",
            color_name="violet-70",
        )   
        # RENDER THE PLOTLY RADAR FIGURE
        st.plotly_chart(self.make_ethics_radar(), use_container_width=True)

        colored_header(
            label="Identified Risks",
            description="Read about the reasoning behind the measured risk scores.",
            color_name="violet-70",
        )        
        for ethics_dim, risk_dict in self.ethics_dimensions.items():
            st.markdown(f"**{risk_dict['display_name']}:**")
            with st.expander(risk_dict['risk_short']):
                st.write(risk_dict["risk"])