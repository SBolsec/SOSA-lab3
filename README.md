# SOSA-lab3

## 1. Running unit tests
```bash
python -m unittest discover -s ./src -p "*test_*.py"
```

## 2. Running bandit static analysis
```bash
bandit -r ./src -f json -o ./logs/bandit.json
```

## 3. Jenkins

### 3.1. Installation

#### 3.1.1. Create a bridge network in Docker

```bash
docker network create jenkins
```

#### 3.1.2. Run a docker:dind Docker image

```bash
docker run --name jenkins-docker --rm --detach \
  --privileged --network jenkins --network-alias docker \
  --env DOCKER_TLS_CERTDIR=/certs \
  --volume jenkins-docker-certs:/certs/client \
  --volume jenkins-data:/var/jenkins_home \
  --publish 2376:2376 \
  docker:dind --storage-driver overlay2
```
#### 3.1.3. Customize official Jenkins Docker image, by executing below two steps:

Create Dockerfile with the following content:

```dockerfile
FROM jenkins/jenkins:2.332.3-jdk11
USER root
RUN apt-get update && apt-get install -y lsb-release
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce-cli
USER jenkins
RUN jenkins-plugin-cli --plugins "blueocean:1.25.3 docker-workflow:1.28"
```

Build a new docker image from this Dockerfile and assign the image a meaningful name

```bash
docker build -t myjenkins-blueocean:2.332.3-1 .
```

#### 3.1.4. Run your own `myjenksing-blueocean:2.332.3-1` image as a container in Docker sing the following `docker run` command

```bash
docker run --name jenkins-blueocean --restart=on-failure --detach \
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  myjenkins-blueocean:2.332.3-1
```
