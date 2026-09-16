import streamlit as st
import os
from src.agentic_ai.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(), layout="wide")
        st.title(self.config.get_page_title())
        st.sidebar.title("Options")
        llm_options = self.config.get_llm_options()
        usecase_options = self.config.get_usecase_options()
        model_options = self.config.get_model_options()
        api_key = st.sidebar.text_input("Enter your API Key:", type="password")


        selected_llm = st.sidebar.selectbox("Select LLM", llm_options)
        selected_usecase = st.sidebar.selectbox("Select Use Case", usecase_options)
        selected_model = st.sidebar.selectbox("Select Gemini Model", model_options)
        

        st.write(f"Selected LLM:- { selected_llm}")
        st.write(f"Selected Use Case:- { selected_usecase}")
        st.write(f"Selected Gemini Model:- { selected_model}")

        return {
            "selected_llm": selected_llm,
            "selected_usecase": selected_usecase,
            "selected_model": selected_model,
            "api_key": api_key
        }

