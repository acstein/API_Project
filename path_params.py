from fastapi import FastAPI

app = FastAPI() 

@app.get("/items/{item_id}") # the value of path parameter item_id will be passed to the function
async def read_item(item_id: int): # going to  http://127.0.0.1:8000/items/foo
    return {"item_id": item_id} # will show item_id: foo (prior to type enforcement)

# path operations are evulated in order so it's important to be
# mindful. In the example below, /users/me would match with 
# /users/{user_id} first if it was above, thinking that the user was me
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# path operations can also be redefined:
@app.get("/users") # this first one will always be used as it matches first
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]

"""
Enum class
- if you want a possible valid path parameter to be predefined
"""
from enum import Enum

class ModelName(str, Enum): # inheriting str is important for API docs
    alexnet = "alexnet" # avaiable valid values
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet: # get value with enum.value
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

"""
What if you want to declare a path parameter containing a path
"""
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}