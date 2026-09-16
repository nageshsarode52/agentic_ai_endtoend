import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage


class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message=None, messages=None, model=None):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message
        self.messages = messages or []
        self.model = model

    @staticmethod
    def _content_to_text(content):
        if isinstance(content, str):
            return content
        if isinstance(content, list):
            return "".join(
                block.get("text", "")
                for block in content
                if isinstance(block, dict)
            )
        return str(content)

    def display_chat_history(self):
        for message in self.messages:
            role = "user" if isinstance(message, HumanMessage) else "assistant"
            with st.chat_message(role):
                st.write(self._content_to_text(message.content))

    def display_result_on_ui(self):
        if self.usecase != "Basic Chatbot":
            return None

        with st.chat_message("user"):
            st.write(self.user_message)

        messages = [*self.messages, HumanMessage(content=self.user_message)]
        response_text = ""

        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            for chunk in self.model.stream(messages):
                response_text += self._content_to_text(chunk.content)
                response_placeholder.markdown(response_text)

        return AIMessage(content=response_text)


