from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates

from contextrain.indexer import index_project
from contextrain.llm import generate_answer
from contextrain.memory import chunk_text, read_file
from contextrain.search import search_chunks


app = FastAPI()

templates = Jinja2Templates(directory="contextrain/templates")

PROJECT_PATH = "."


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"answer": None},
    )


@app.post("/ask")
def ask(request: Request, question: str = Form(...)):
    files = index_project(PROJECT_PATH)

    all_chunks = []

    for file in files:
        content = read_file(file)
        chunks = chunk_text(content)
        all_chunks.extend(chunks)

    relevant_chunks = search_chunks(question, all_chunks)

    answer = generate_answer(question, relevant_chunks)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"answer": answer},
    )