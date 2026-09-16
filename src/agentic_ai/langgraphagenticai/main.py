import streamlit as st
from langchain_core.messages import HumanMessage
from src.agentic_ai.langgraphagenticai.ui.streamlit.loadui import LoadStreamlitUI
from src.agentic_ai.langgraphagenticai.LLMS.geminillm import GeminiLLM
from src.agentic_ai.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.agentic_ai.langgraphagenticai.ui.streamlit.displayresult import DisplayResultStreamlit



def load_langgraph_agenticai_app():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    ui_loader = LoadStreamlitUI()
    user_input  = ui_loader.load_streamlit_ui()

    if not user_input:
        st.error("Error: No user input received. Please provide the required inputs.")
        return 
    history_display = DisplayResultStreamlit(
        usecase=user_input.get("selected_usecase"),
        graph=None,
        messages=st.session_state.messages,
    )
    history_display.display_chat_history()

    user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            # Configure LLM 
            obj_llm_config = GeminiLLM(user_control_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initialised")
                return 
            # Setup use case
            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("Error: No use case selected")
                return 
            # Graph Builder
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                response = DisplayResultStreamlit(
                    usecase,
                    graph,
                    user_message,
                    st.session_state.messages,
                    model,
                ).display_result_on_ui()
                st.session_state.messages.extend(
                    [HumanMessage(content=user_message), response]
                )
            except Exception as e:
                st.error(f"Error: Graph set up failed - {e}")
                return
        except Exception as e:
            st.error(f"Error: Graph set up failed - {e}")
            return



