# syntax=docker/dockerfile:1.4
# FROM --platform=$BUILDPLATFORM python:3.10-alpine
FROM python:3.8

RUN apt update \
    && pip install --upgrade pip

WORKDIR /app

# set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN apk add build-base \
# RUN pip install --upgrade pip

# RUN pip install -U scikit-learn

# install the requirements (requirements.txt have to exists on localhost)
COPY ./requirements.txt .
# RUN --mount=type=cache,target=/root/.cache/pip \
RUN pip install -r requirements.txt

COPY . .

# initialize the database (create DB, tables, populate)
# RUN python init_db.py

EXPOSE 5000/tcp

# CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]
# CMD ["flask", "run"]
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--debug"]
# CMD ["python", "./main.py"]
