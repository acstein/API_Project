from fastapi import FastAPI

app = FastAPI() # create an instance of the fastapi class

"""
this is a path operation decorator
it tells FastAPI that the function below is in charge of
requests that go to the path ('/') using GET
typically the path is everything after a URL starting from
the first /.
the path separates concerns and resources?
operations in are typically:
POST, GET, PUT, DELETE
"""
@app.get('/') 

"""
This is the path operation function.
The path is /.
The operator is get
the function is below. It's called by FastApi whenever it receives
a request to the URL '/' using a GET operation
"""
async def root(): # here it is an async function but this can be omitted
    return {'message': 'Hello World'}
"""
Finally, the content is returned.
"""