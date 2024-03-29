FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10
COPY /app/requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY ./model /model/
COPY ./app /app