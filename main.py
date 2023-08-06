from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from chat import initialiseTutor, chatWithTutor
from schema import Info, Message
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Define the origins that are allowed to access your API (you can use "*" to allow all origins)
origins = [
    "http://localhost",
    "http://localhost:8501",  # Replace this with the actual frontend URL
]

# Enable CORS using the CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({
            "detail": exc.errors(), 
            "body": exc.body}),
    )

@app.post("/info")
async def info(info:Info):
    print("Information Received")
    info = info.dict()
    subtopic,concept,blooms_level,lo = info['selectedTopic'], info['selectedConcept'], info['bloomsLevel'], info['learningOutcome']
    return initialiseTutor(subtopic,concept,blooms_level,lo)

@app.post("/chat")
async def chatFun(message:Message):
    print("New Message Received")
    message = message.dict()
    message= message['message']
    return chatWithTutor(message)

