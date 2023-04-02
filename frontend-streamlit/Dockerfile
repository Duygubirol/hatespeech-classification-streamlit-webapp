FROM python:3.9

WORKDIR /frontend

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

EXPOSE 8001

ENTRYPOINT ["streamlit", "run", "./app/streamlit_app.py", "--server.port=8001", "--server.address=0.0.0.0"]