#!/bin/bash

# To run from PROD server
git pull

# build new image, stop running container (make ports free) and run new image
docker build -t ocr_libraries:latest .
# docker stop ocr_libraries
# docker rm ocr_libraries  # error to fix
docker run -p 5000:5000 --rm --name "ocr_libraries" -v ./:/app/ ocr_libraries:latest   # -d

# todo to TEST..
# inside container
# $ pip install -r requirements.txt