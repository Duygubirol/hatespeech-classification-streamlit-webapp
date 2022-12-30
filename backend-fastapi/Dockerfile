FROM python:3.9

WORKDIR /backend

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

EXPOSE 8000

# cd to the folder contaning fastapi_app.py
WORKDIR /backend/app
CMD python -m uvicorn fastapi_app:app --host 0.0.0.0 --port 8000

# CMD ["python", "./app/fastapi_app.py"]
