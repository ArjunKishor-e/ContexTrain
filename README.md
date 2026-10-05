ContexTrain

ContexTrain is an AI context manager for developers. It searches a project's files and provides relevant context to an AI model before generating an answer.

Features
Indexes project files
Splits files into chunks
Uses Sentence Transformers for semantic search
Uses cosine similarity to find relevant context
Retrieves the top 10 relevant chunks
Uses Llama 3.2 locally through Ollama
Simple FastAPI and Jinja2 web interface
Tech Stack
Python
FastAPI
Jinja2
Sentence Transformers
scikit-learn
Ollama
Llama 3.2
Setup

Clone the repository:

git clone https://github.com/ArjunKishor-e/ContexTrain.git
cd ContexTrain

Create a virtual environment:

python -m venv .venv
.venv\Scripts\activate

Install the dependencies:

pip install -r requirements.txt

Install and run Ollama, then pull the model:

ollama pull llama3.2:3b

Start the application:

python -m uvicorn contextrain.main:app --reload

Then open:

http://127.0.0.1:8000/