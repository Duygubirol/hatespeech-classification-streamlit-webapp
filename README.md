# hate-speech-detection-streamlit-app


## cmd to run docker from terminal
docker run -p 8000:8000 helloworld-backend
docker run -p 8001:8001 helloworld-frontend
docker compose up --build 


## run streamlit app
streamlit run ./app/streamlit_app.py --server.port=8001 --server.address=0.0.0.0

## run uvicorn fastapi app (go to all folder first)
python -m uvicorn fastapi_app:app --host 0.0.0.0 --port 8000


## Ref:
https://www.youtube.com/watch?v=HG6yIjZapSA


https://blog.jcharistech.com/2022/08/05/deploying-streamlit-and-fastapi-apps-using-docker-and-docker-compose/

How to saved and load models with Transformer TFTrainer
https://stackoverflow.com/questions/64663385/saving-and-reload-huggingface-fine-tuned-transformer

How to deploy Docker to Google Cloud Run:
https://www.syndicai.co/blog/deploy-ml-model-with-fastapi
https://github.com/sekR4/FastAPI-on-Google-Cloud-Run
