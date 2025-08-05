from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
conn = MongoClient("mongodb-Url")

print("Server is starting...")

db = conn["noteDb"]
collection = db["notes"]

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notesDb.notes.find_one({})
    print("Document from DB:", docs)
    return templates.TemplateResponse(
        "index.html", {"request": request, "note": docs}
    )

@app.get("/insert")
def insert_sample():
    sample = {"title": "Hello", "content": "This is a sample note"}
    result = collection.insert_one(sample)
    return {"inserted_id": str(result.inserted_id)}