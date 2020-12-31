# Developement Environement

## Prerequisites

Developement environment is setup using Docker Compose, you need to install some tools before you proceed.

1. Install [Docker](https://docs.docker.com/install/).
2. Install [Docker Compose](https://docs.docker.com/compose/install/#install-compose) (compose file format version `2.1` minimum)

/!\ Attention Windows Subsytem Linux users! In order to use volumes, some tweaks are needed. /!\

```bash
$ ➜ sudo mount --bind /mnt/c /c
$ ➜ cd /c/path/to/project/docker-compose
$ ➜ export COMPOSE_CONVERT_WINDOWS_PATHS=1
```

*It has to be done for each terminal.*

## Local Architecture

Developement environment will be compose by a set of containers:

1. Jupyter notebook

Data and notebooks are stored in `data` and `workdir` folders.

```bash
$ ➜ mkdir data workdir
$ ➜ sudo chmod -R 777 data workdir
```

## Generate access token

```bash
$ ➜ touch .env
$ ➜ py generate_token.py -p password
Generate a access token

Copy this line into the .env file:

ACCESS_TOKEN=[token]
```

Copy the line `ACCESS_TOKEN=...` in the `.env` file.

## Build developement environment

Before you start, Check that you've all [prerequisites](#prerequisites) installed in your machine.

### Launch the rocket

```bash
$ ➜ docker-compose up -d
```

### List containers

To list containers and port-forwarding information:

```bash
$ ➜ docker-compose ps
```

### Connect to a container for Debug

To connect inside one of these containers:

```bash
$ ➜ docker exec -it jupyter_notebook bash
(base) jovyan@e91275158bad:~$ 
```

### Logs

To print logs for a specific container run:

```bash
$ ➜ docker-compose logs -f jupyter_notebook
```

### Stop, start and restart

```bash
$ ➜ docker-compose [start,stop,restart] jupyter_notebook
```

### For more details

```bash
$ ➜ docker-compose --help
```