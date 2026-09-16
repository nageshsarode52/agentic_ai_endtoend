from typing import List, Dict, Any
from langgraph.graph.message import add_messages
from typing import TypedDict
from typing_extensions import Annotated

class State(TypedDict):
    """
    Represents the state of the application, including user input and messages.
    """
    messages: Annotated[List, add_messages]
