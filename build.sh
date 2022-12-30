#!/usr/bin/env bash

# Build image
docker build --tag=clickecho .

# List docker images
docker image ls

#Run Container
docker run -it clickecho python app.py --name "Ertan"