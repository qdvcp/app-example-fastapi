from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/hi", response_class=PlainTextResponse)
async def root():
    return "Timeweb Cloud + FastAPI = ❤️"
