# syntax=docker/dockerfile:1.4
FROM python:3.8

WORKDIR /app

RUN apt-get update \
    && apt-get install -y build-essential libpoppler-cpp-dev pkg-config  \
    && pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000/tcp

CMD ["python", "app.py"]