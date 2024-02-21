#!/bin/bash

# To run from PROD server
git pull

# build new image, stop running container (make ports free) and run new image
docker build -t chatbot-gpt-35:latest .
# docker stop chatbot-gpt-35
# docker rm chatbot-gpt-35  # error to fix
docker run -p 5000:5000 --rm --name "chatbot-gpt-35" -v ./:/app/ chatbot-gpt-35:latest   # -d

# todo to TEST..
# inside container
# $ pip install -r requirements.txt