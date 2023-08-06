import warnings
from dotenv import load_dotenv, find_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain.memory import ConversationSummaryBufferMemory
from langchain import ConversationChain
from langchain.chat_models import ChatOpenAI
from instructions import getInstructions

# Load OpenAI API key and pass it into env
_ = load_dotenv(find_dotenv()) 
warnings.filterwarnings('ignore')



def initialiseTutor(subtopic,concept,blooms_level,lo):
    """
    Function to initialize LLM by providing required instructions.
    Parameters:
    subtopic: JavaScript Subtopic
    concept: JS Concept
    blooms_level: Student's blooms_level
    lo: Learning Outcome
    """

    template1 = getInstructions()

    template2 = f"""
    <Topic : Javascript , Sub Topic : {subtopic} , Concept : {concept} \
    Blooms level : {blooms_level} , Learning Outcome : {lo}>
    """

    template3 = """
    Current conversation:
        {history}
        Human: {input}
        AI tutor:   
    """

    template = template1+template2+template3

    llm =  ChatOpenAI(temperature=0.9)
    PROMPT = PromptTemplate(input_variables=["history", "input"], template=template)
    memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=4000, ai_prefix="AI tutor")
    global conversation
    conversation = ConversationChain(
        prompt=PROMPT,
        llm=llm,
        verbose=False,
        memory=memory
    )

    return conversation.predict(input="Start")


def chatWithTutor(message):
    """
    Function of having coversation with the LLM.
    Parameters:
    message: Input message from the user to the LLM.
    """
    
    return conversation.predict(input=message)
