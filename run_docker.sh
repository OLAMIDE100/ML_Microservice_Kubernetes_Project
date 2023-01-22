

# Step 1:
docker build  docker/  --tag house_predict

# Step 2: 
docker image ls

# Step 3: 
docker run --rm -it --name housing_price_api -p 8000:80 house_predict
