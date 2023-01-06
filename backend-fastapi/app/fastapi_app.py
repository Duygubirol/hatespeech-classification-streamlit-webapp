# https://medium.com/codex/streamlit-fastapi-%EF%B8%8F-the-ingredients-you-need-for-your-next-data-science-recipe-ffbeb5f76a92
# https://levelup.gitconnected.com/fastapi-fundamentals-getting-faster-with-fastapi-866545b841ca

import uvicorn
from fastapi import FastAPI
# this intra package import path is made as Docker run from /app folder
from model.utils import make_prediction
from pydantic import BaseModel


class input_schema(BaseModel):
    input_text: str


app = FastAPI()


@app.get("/")
def health_check():
    return 'Hello World'


@app.post("/predict")
def operate(input: input_schema):
    # input.input_text will return just the text value from the json format
    result = make_prediction(input.input_text)
    return result


# if __name__ == '__main__':
#     uvicorn.run(app, port=8001, host='0.0.0.0')