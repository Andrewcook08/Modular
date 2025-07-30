from fastapi import FastAPI, Body
import uvicorn
import os

app = FastAPI()
CODE_STORE = "examples/simple_app.py"

@app.get("/context")
def get_context():
    with open(CODE_STORE, "r") as file:
       return {"code": file.read()}
    
@app.post("/update")
def update_context(new_code: str = Body(...)):
    with open(CODE_STORE, "w") as file:
        file.write(new_code)
    return{"status": "updated"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)