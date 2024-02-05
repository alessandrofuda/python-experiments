# syntax=docker/dockerfile:1.4
# FROM --platform=$BUILDPLATFORM python:3.10-alpine
FROM python:3.8

WORKDIR /app

# set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# RUN apk add build-base \
RUN pip install --upgrade pip

# !! IMP !!
RUN pip install -U scikit-learn

# install the requirements
COPY requirements.txt /app
# RUN --mount=type=cache,target=/root/.cache/pip \
RUN pip3 install -r requirements.txt

COPY . .

# initialize the database (create DB, tables, populate)
# RUN python init_db.py

EXPOSE 5000/tcp

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]
# CMD ["flask", "run"]
