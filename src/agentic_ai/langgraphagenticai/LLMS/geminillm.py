import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI


class GeminiLLM:
    def __init__(self, user_control_input):
        self.user_control_input = user_control_input

    def get_llm_model(self):
        google_api_key = self.user_control_input.get("api_key")
        selected_model = self.user_control_input.get("selected_model")

        if not google_api_key:
            st.error("Error: Google AI Studio API key is required to initialize Gemini.")
            return None

        try:
            return ChatGoogleGenerativeAI(
                google_api_key=google_api_key,
                model=selected_model,
                temperature=0.2,
            )
        except Exception as error:
            st.error(f"Error initializing Gemini: {error}")
            return None
