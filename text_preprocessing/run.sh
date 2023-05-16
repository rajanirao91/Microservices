docker build -t text-preprocess-microservice .
docker run -p 5000:5000 -v $(pwd)/app/resources/config.yaml:/app/resources/config.yaml -v $(pwd)/app/logs:/app/logs text-preprocess-microservice
