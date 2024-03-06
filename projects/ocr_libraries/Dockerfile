# syntax=docker/dockerfile:1.4
FROM python:3.8

WORKDIR /app

RUN apt-get update \
    && apt-get install -y build-essential libpoppler-cpp-dev pkg-config  \
    && pip install --upgrade pip

RUN groupadd -g 1000 www \
    && useradd -u 1000 -ms /bin/bash -g www www \
    && usermod -a -G www www-data

USER www

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000/tcp

CMD ["python", "app.py"]