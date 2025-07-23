# Parser API Project

A simple **FastAPI** project that provides:
- A **`/hello`** endpoint (basic GET test).
- An **`/echo`** endpoint (POST endpoint that returns the text you send it).
- **Error handling** (rejects empty or whitespace-only text).
- **Unit tests** with `pytest` (no need for a live server).

This project was created as part of a month-long learning sprint to explore **backend development with Python**.

---

## Features
- **FastAPI** framework with automatic interactive docs (`/docs`).
- **Error handling** using `HTTPException`.
- **Unit tests** using FastAPI's `TestClient` and `pytest`.
- Ready for extension (e.g., adding parsers, databases, or more endpoints).

---

## Project Structure
API_Project/
│
├── my_first_api.py # FastAPI app with /hello and /echo endpoints
├── test_.py # Unit tests for the API
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## Installation & Setup

### 1. Clone the repository
git clone https://github.com/acstein/API_Project

### 2. Create a venv
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows

### 3. install dependencies
pip install -r requirements.txt

## Running the App
Start the FastAPI server:
uvicorn my_first_api:app --reload
fastapi dev my_first_api.py

Visit:
- Swagger UI: http://127.0.0.1:8000/docs
- Hello endpoint: http://127.0.0.1:8000/hello

## Running Tests
Run all tests:
pytest -v

You should see:
test_.py::test_hello PASSED
test_.py::test_echo_valid PASSED
test_.py::test_echo_empty PASSED

