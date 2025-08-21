from langchain_openai import ChatOpenAI
from langchain_core.caches import BaseCache  # make sure BaseCache is defined


class ResearchAgent:
    def __init__(self, model_name="gpt-4o", temperature=0.7):
        # Fix Pydantic v2 rebuild
        ChatOpenAI.model_rebuild(force=True)
        self.llm = ChatOpenAI(model=model_name, temperature=temperature)

    def run(self, query: str) -> str:
        return self.llm.invoke(query)
