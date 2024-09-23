from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Comment
@app.get("/")
async def welcome():
    try:
        return {"message": "hello from server"}
    except Exception as e:
        print(f'Exception: {e}')
        raise HTTPException(status_code=500, detail=str(e))
@app.get("/test")
async def hello():
    try:
        return {"message": "hello from test server"}
    except Exception as e:
        print(f'Exception: {e}')
        raise HTTPException(status_code=500, detail=str(e))