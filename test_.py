from fastapi.testclient import TestClient
from my_first_api import app

# Create a test client that behaves like a fake browser calling your API
client = TestClient(app)

def test_hello():
    """
    Test that GET /hello returns status 200
    and the correct JSON message.
    """
    response = client.get("/hello")
    assert response.status_code == 200  # The endpoint should return OK
    assert response.json() == {'message': 'Oh hello there!'}

def test_echo_valid():
    """
    Test that POST /echo with valid text
    returns status 200 and the same text.
    """
    response = client.post("/echo", json={"text": "Hello"})
    assert response.status_code == 200
    assert response.json() == {"received_text": 'Your text was: "Hello" here is your response!'}

def test_echo_empty():
    """
    Test that POST /echo with an empty string
    returns a 400 Bad Request with the correct error message.
    """
    response = client.post("/echo", json={"text": ""})
    assert response.status_code == 400
    assert response.json() == {"detail": "Text cannot be empty."}

def test_echo_whitespace():
    """
    Test that POST /echo with only whitespace
    is treated as invalid input (same as empty).
    """
    response = client.post("/echo", json={"text": "   "})
    assert response.status_code == 400
    assert response.json() == {"detail": "Text cannot be empty."}

