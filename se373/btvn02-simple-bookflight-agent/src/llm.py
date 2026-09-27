from langchain_openai import ChatOpenAI 
import os

from pydantic import SecretStr

from src.tool_registry import tools


llm = ChatOpenAI(
    model = "paste-your-model-id-here",
    api_key=SecretStr("paste-your-api-key-here"),
    base_url="https://openrouter.ai/api/v1",  #Open Router Provider
    temperature=0,
)

llm_with_tools = llm.bind_tools(tools)