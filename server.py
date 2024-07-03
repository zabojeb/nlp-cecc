from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import requests
from model import process_url

app = FastAPI()


# Загрузите ваши модели заранее


class UrlRequest(BaseModel):
    url: str


@app.post("/process-url")
def process_url_endpoint(request: UrlRequest):
    url = request.url
    try:
        # Пример обработки с использованием первой модели
        result = process_url(url)
        return {'result': result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
