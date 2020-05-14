# GSU Docker Demonstration

This repository contains the materials for the Docker demonstration that was presented on May 6th, 2020 to the [Evidence-based Cybersecurity](https://ebcs.gsu.edu/) research group at [Georgia State University](https://ebcs.gsu.edu/). The demo consisted of four parts which are outlined below.

## Demo 0

This demo showed the use of typical Docker commands for pulling and running images. The following commands were used (with their purpose annotated on the right):

```shell
docker info                                 - show Docker system information
docker images                               - show downloaded Docker images
docker ps                                   - show running containers
docker ps -a                                - show all containers (running and stopped)
docker run -it --rm archlinux /bin/bash     - run the Bash shell in an interactive Arch Linux container
docker create --name demo-arch archlinux    - create a named container using the Arch Linux image
```

## Demo 1

This demo showed the use of a basic Dockerfile for the purpose of creating a custom Docker image with specific software installed. To run this demo, simply do the following:

```shell
cd demo1
docker build -t demo1/tensorflow-keras .
docker run --rm -d -p 8888:8888 -v $(pwd):/code -w /code demo1/tensorflow-keras
```

This will run the container in the background. It exposes port `8888` on the host and maps it to port `8888` in the container. It also maps the current working directory to the `/code` directory in the container and sets that directory as the working directory. To follow the log output, run `docker logs -f <container id>` using the container id obtained from running `docker ps`. To stop the container, simply run `docker stop <contained id>`.

## Demo 2

This demo showed the use of the `docker-compose` tool in conjunction with a `Dockerfile` for the purpose of running a simple Flask web application. To run this demo, simply do the following:

```shell
cd demo2
docker-compose up -d --build
```

As with the first demo, the log output of the containers can be followed using `docker-compose logs -f`. To stop the container, run `docker-compose down`.

## Demo 3

This final demo showed how to compose multiple services using the `docker-compose` YAML syntax. This demo shows how to run multiple services and connect them together to compose a single application. The Nginx web server container is used as a reverse proxy to the Flask application container. The Flask container uses a MariaDB container for a database backend. This demo needs some additional set up before running it. Assuming you use the default `/opt/docker/demo/demo3/` local volume, do the following:

```shell
cd demo3
mkdir -p /opt/docker/demo/demo3/nginx/nginx/site-confs
cp nginx.conf /opt/docker/demo/demo3/nginx/nginx/site-confs/default
mkdir -p /opt/docker/demo/demo3/mariadb/initdb.d
cp db.sql /opt/docker/demo/demo3/mariadb/initdb.d
```

The first file is the Nginx configuration to enable reverse proxying requests to the Flask container. The second file is a database seed file that will create the table for storing data and insert a few records into it. You're now ready to bring the services up.

```shell
cd demo3
docker-compose up -d --build
```

As with the previous demo, the log output of the containers can be followed using `docker-compose logs -f`. To stop the container, run `docker-compose down`.

Notice the service configuration in the `docker-compose.yml` file exposes only the Nginx web server (on port 8002). Neither the Flask application nor the database backend have ports exposed. The network that is created allows all of the services to communicate with each other. Creating this network isn't mandatory since all Docker containers are given an IP address internally. However, it makes more explicit the ability to link services together while limiting external access to services as needed.

## Installing Docker

Windows and Mac users can install Docker Desktop from here: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/). Note that you'll also need a working installation of Virtualbox, which can be downloaded here: [https://www.virtualbox.org/](https://www.virtualbox.org/)

The preferred way to run Docker is natively on a Linux system. Digital Ocean has a great set of guides for installing Docker on several different Linux distributions here:  [https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04)

We also made use of the `docker-compose` utility. Installation instructions are here:  [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

## Misc

A Pipfile is included for use with the [pipenv](https://pipenv.pypa.io/) utility for development. It's possible to edit the code in the `demo2` and `demo3` directories before launching their respective services. This is similar to what might be encountered in a typical software development shop.

A recording of the presentation was made. Send [me a note](mailto:cfreas@cs.gsu.edu) and I'll share the link with you.
