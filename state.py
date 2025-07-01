from typing import TypedDict, List, Optional
from langchain.schema import Document


class FAQState(TypedDict):
    question: str
    retrieved_docs: Optional[List[Document]]
    condition: Optional[str]
    followup: Optional[str]
    answer: Optional[str]
