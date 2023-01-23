#!/usr/bin/env bash
# This file tags and uploads an image to Docker Hub

# Assumes that an image is built via `run_docker.sh`

# Step 1:
# Create dockerpath
dockerpath=midecreative1994/house_predict:latest

# Step 2:  
# Authenticate & tag
echo "Docker ID and Image: $dockerpath"

docker login -u midecreative1994 -p "$DOCKER_PASSWORD"

docker tag house_predict:latest "$dockerpath"

# Step 3:
# Push image to a docker repository
docker push "$dockerpath"
