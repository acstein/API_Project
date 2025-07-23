from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get('/hello')
def hello_response():
    """
    A simple GET endpoint.
    When you visit /hello, it returns a JSON greeting.
    """
    return {'message': 'Oh hello there!'}

class EchoInput(BaseModel):
    # Define the data model for the POST /echo endpoint
# This enforces that the request body must have a "text" field (string)
    text: str

@app.post('/echo')
def echo(input_data: EchoInput):
    """
    A POST endpoint that receives JSON input ({"text": "some text"})
    and returns the same text back as JSON.

    Error handling: If the text is empty or just spaces, raise a 400 error.
    """
    if not input_data.text.strip(): # strip handles the user only inputting whitespace
        raise HTTPException(status_code=400, detail='Text cannot be empty.')
    return {'received_text': 'Your text was: "' + input_data.text + '" here is your response!'}