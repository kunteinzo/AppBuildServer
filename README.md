# Build Android Studio Project in Command Line Terminal

## Build Docker Image and Run Container

```bash
# Build the image
docker build -t appbuild .

# Run Container
docker run -it -p 8000:8000 --name appbuild appbuild

# Enter Container Shell
docker exec -it appbuild /bin/bash

# Start the stopped container
docker start appbuild

# Stop running container
docker stop appbuild

# Remove container
docker rm appbuild

# Remove image
docker rmi appbuild

# Clear stuff (free up space)
docker container prune
docker image prune
docker builder prune
```

## API 

- End point: `/cmd`
  Method: `POST`
  Content-Type: `application/json`
  Body: `{"cmd": ["echo", "hello"]}`
  Response: `{"output": "success output", "error": "Error output"}`
  Usage: To test execute command from API

- End point: `/build`
  Method: `GET`
  Response: `{"output": "success output", "error": "Error output"}`

- End point: `/getApp`
  Method: `GET`
  Response: Build Apk File if build success else "App haven't build yet"

