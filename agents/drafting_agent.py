from langchain_openai import ChatOpenAI

class DraftingAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    def draft_motion(self, motion_type="modify_timesharing"):
        prompt = f"Draft a {motion_type} motion for Respondent Melanie Vaughn in Florida family court."
        return self.llm.invoke(prompt).content
