FROM python:3.8-slim-buster

## Step 1:
WORKDIR /app

## Step 2:
COPY ./app.py /app
COPY ./requirements.txt /app
RUN mkdir model_data
COPY ./model_data/boston_housing_prediction.pkl /app/model_data

## Step 3:
RUN pip install  -r  requirements.txt 

# hadolint ignore=DL3013

## Step 4:
EXPOSE 80

## Step 5:
CMD [ "python", "app.py" ]

