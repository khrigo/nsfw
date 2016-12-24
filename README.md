# NSFW

This project uses Yahoo Open NSFW (Not Safe For Work) to detect images that contain pornographic content. OpenNSFW uses Caffe pretrained neural network models and has a very big success rate.

The output is a float number from 0 to 1. Scores above 0.8 are NSFW. Everything below 0.2 is completely clean.

## Installation

### Build docker from Dockerfile
```
docker build -t nsfw .
```

### Run server on 5000 port from docker
```
docker run -p 5000:80/tcp nsfw
```

## Example
### Send cURL request with image on server
```
curl -X POST -F "image=@test.jpg" http://localhost:5000/nsfw
```
