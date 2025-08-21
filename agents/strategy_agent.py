from langchain_openai import ChatOpenAI

class StrategyAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    def build_strategy(self):
        prompt = """You are StrategyAgent. Build a litigation strategy for Melanie Vaughn.
        Goals: reinstate communication, then supervised timesharing, eventually shared custody.
        Consider: Florida statutes, expedited hearing rights, rehab proof, attacking hearsay.
        Output in bullet points grouped as Short-Term vs Long-Term."""
        return self.llm.invoke(prompt).content
