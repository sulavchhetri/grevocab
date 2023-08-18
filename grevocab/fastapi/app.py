"""
    This module is used to return the api of details of words
"""
import os
import json
from pathlib import Path
import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from grevocab.fastapi.util import PrettyJSONResponse
from grevocab.main import scrape_words

gre_files_path = os.path.join(
    Path(__file__).parent.parent.parent, "files", "gregmat.json")

templates_path = os.path.join(Path(__file__).parent, "templates")
app = FastAPI()

templates = Jinja2Templates(directory=templates_path)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def process_get(request: Request):
    """
        This function is used to display the form template to the user
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/", response_class=PrettyJSONResponse)
def process(words: str = Form()):
    """
        This function take the form data, performs a function on it and returns
        the result
    """
    if not words:
        return {"data": None}
    words_list = words.split(',')
    return {'data': scrape_words(words=words_list)}


@app.get("/gregmat", response_class=PrettyJSONResponse)
def get_gregmat_words():
    """
        This function renders the gregmat data.
    """
    with open(gre_files_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, host="0.0.0.0", port=5000)
