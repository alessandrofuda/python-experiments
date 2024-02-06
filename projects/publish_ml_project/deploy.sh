#!/bin/bash

# To run from PROD server
git pull

# build new image, stop running container (make ports free) and run new image
docker build -t test-python-app:latest .
docker stop test-python-app
docker rm test-python-app
docker run -d -p 5000:5000 --rm --name "test-python-app" test-python-app:latest

# todo to TEST..