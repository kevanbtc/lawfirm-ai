from pypdf import PdfReader
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

class IntakeAgent:
    def __init__(self, case_path: str):
        self.case_path = case_path
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    def extract_text(self, max_pages=5):
        reader = PdfReader(self.case_path)
        text = ""
        for page in reader.pages[:max_pages]:
            text += page.extract_text() + "\n"
        return text

    def extract_timeline(self):
        raw = self.extract_text()
        template = PromptTemplate.from_template("""
        You are IntakeAgent for a family law case. Summarize the following into:
        - Case number
        - Parties
        - Key events & dates (timeline)
        - Allegations
        - Orders
        Text:
        {raw}
        """)
        return self.llm.invoke(template.format(raw=raw)).content
