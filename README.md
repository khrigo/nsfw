# NSFW

Soon...

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
