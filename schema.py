from pydantic import BaseModel

class Info(BaseModel):
    selectedTopic: str
    selectedSubtopic: str 
    selectedConcept: str
    bloomsLevel: str 
    learningOutcome: str 

class Message(BaseModel):
    message: str