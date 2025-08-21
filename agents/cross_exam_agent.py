from langchain_openai import ChatOpenAI

class CrossExamAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    def build_questions(self, witness="anthony"):
        prompt = f"""
        You are CrossExamAgent. Generate cross-examination questions for witness: {witness}.
        Focus on credibility, bias, inconsistencies, hearsay, and alternative explanations.
        Case: Puglisi v. Vaughn, Palm Beach, FL.
        """
        return self.llm.invoke(prompt).content
