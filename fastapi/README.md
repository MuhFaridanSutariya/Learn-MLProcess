# Docker Setup and Usage

This repository provides instructions on how to build and run a Docker image. Before proceeding, ensure that Docker is installed on your Ubuntu system.

## Installation

Follow the official Docker documentation to install Docker on Ubuntu by following the step-by-step instructions provided at [https://docs.docker.com/engine/install/ubuntu/](https://docs.docker.com/engine/install/ubuntu/).

## Building the Docker Image

To build the Docker image, navigate to the directory containing the Dockerfile and run the following command:

```bash
docker build -t example_cicd .
```
Replace `example_cicd` with the desired tag name for your Docker image.

The build process will start, and Docker will execute the instructions specified in the Dockerfile to create the image.

## Running Fastapi on Docker Image
```bash
docker run -p 8009:8000 pacmann_mlprocess_api uvicorn src.api.main:app --host 0.0.0.0
```

This command will start a container and bind port 8009 of the host machine to port 8000 of the container. The `uvicorn` command is used to run the specified Python application within the container.

You can now access the running application by opening a web browser and navigating to `http://localhost:8009`.

Note: If you want to run the container in the background (detached mode), you can add the `-d` flag to the `docker run` command.

Illustration of architecture


![image](https://github.com/MuhFaridanSutariya/Learn-MLProcess/assets/88027268/281fc45d-095b-49ad-bfe0-cbd74d50acc4)



