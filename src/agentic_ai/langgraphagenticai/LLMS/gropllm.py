import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_control_input):
        self.user_control_input = user_control_input

    def get_llm_model(self):
        try:
            groq_api_key = self.user_control_input.get("api_key")
            selected_groq_model = self.user_control_input.get("selected_groq_model")
            if not groq_api_key:
                st.error("Error: API Key is required to initialize the Groq LLM.")
                return None
            llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)

        except Exception as e:
                st.error(f"Error initializing Groq LLM: {e}")
        return llm
    