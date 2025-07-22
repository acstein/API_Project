from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/hello')
def hello_response():
    return {'message': 'Oh hello there!'}

class EchoInput(BaseModel):
    text: str

@app.post('/echo')
def echo(input_data: EchoInput):
    return {'received_text': input_data.text + 'very'}