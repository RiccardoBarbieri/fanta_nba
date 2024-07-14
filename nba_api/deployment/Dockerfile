FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY ./venv_req.txt /app/requirements.txt
COPY __init__.py /app/__init__.py

ADD swagger_server /app/swagger_server
ADD geo /app/geo
ADD featurevec /app/featurevec
ADD utils /app/utils

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8124

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--bind=127.0.0.1:8124", "--chdir", "swagger_server", "'app:app()'"]
