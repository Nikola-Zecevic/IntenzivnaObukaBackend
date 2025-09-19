from fastapi import FastAPI, HTTPException, Response, responses
import requests
import datetime
import json
from pydantic import BaseModel
app = FastAPI()

# GET all
# GET by id
# PUT by id
# DELETE by id

class TODO(BaseModel):
    id:int
    text:str



API_URL="https://my-json-server.typicode.com/Nikola-Zecevic/TODObase/todos"

@app.get("/")
def root():
    body="<html>"\
        "<body>"\
        "<h1>Welcome</h1>"\
        "<div>Home route</div>"\
        "</body>"\
        "</html>"
    return responses.HTMLResponse(content=body)#{"message": "Hello World"}


ALL_TODOS=requests.get(API_URL).json()

@app.get("/tasks")
def get_all():
    return ALL_TODOS


@app.get("/tasks/{task_id}")
async def read_item(task_id):
    for item in ALL_TODOS:        
        if int(item["id"])==int(task_id):
            return item

    return responses.JSONResponse(content={"error":"Item not found  "},status_code=400)

@app.put("/tasks/{task_id}")
async def put_item(task_id:int,text:str):
    for item in ALL_TODOS:        
        if int(item["id"])==int(task_id):
            item["text"]=text
            return item
    try:
        ALL_TODOS.append({"id":task_id,"text":f"{text}"})
    except:
        return responses.JSONResponse(content={"error":"Couldn't finish task"},status_code=400)

@app.delete("/tasks/{task_id}")
async def delete_item(task_id):
    global ALL_TODOS
    for item in ALL_TODOS:
        if int(item["id"])==int(task_id):
            ALL_TODOS.remove(item) 
            print(ALL_TODOS)
            return item
    return responses.JSONResponse(content={"error":"Item not found "},status_code=400)
