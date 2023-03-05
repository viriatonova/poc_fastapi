# Cronos API

## Content

1. [Documentation](#documentation)
2. [Dependencies](#dependencies)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Tests](#tests)

## Documentation

* [Database schema](https://dbdiagram.io/d/63f36006296d97641d824880)

## Dependencies

- [Node](https://nodejs.org/en/)
- [Docker](https://docs.docker.com/reference/)
- [Docker-compose](https://docs.docker.com/compose/)

## Setup

* add `.env`:

DEBUG=True
RELOAD=True
API_HOST=0.0.0.0
API_PORT=9000
ALGORITHM=<algorithm>
SECRET_KEY=<secretkey>
DB_SERVER=mysql+pymysql
DB_USER=root
DB_PASSWORD=secret
DB_ROOT_PASSWORD=secret
DB_DATABASE=cronos
DB_HOST=db
DB_PORT=3306

## Usage

## Tests




