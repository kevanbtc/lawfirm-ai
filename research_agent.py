# agents/research_agent.py

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


class ResearchAgent:
    def __init__(self):
        # Initialize ChatOpenAI without model_rebuild hacks
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0
        )

    def run(self, topic: str) -> str:
        """Run legal research on a given topic."""
        prompt = ChatPromptTemplate.from_template(
            "You are a legal research assistant. Research the following topic in detail:\n\n{topic}"
        )
        chain = prompt | self.llm
        return chain.invoke({"topic": topic}).content
