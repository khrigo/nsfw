# NSFW

Soon...

## Installation

### test
```
docker build -t nsfwaas .
```

### test
```
docker run -p 5000:80/tcp nsfwaas
```

### test
```
curl -X POST -F "image=@test.jpg" http://localhost:5000/nsfw
```
