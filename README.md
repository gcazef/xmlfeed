# XMLFeed

XML product feed parser

## Requirements
 - docker
 - docker-compose

## Getting started

First, build the docker image:
```bash
$> docker build .
```

You can then migrate the database and create a superuser:
```bash
$> docker-compose run web python /code/manage.py migrate --noinput
$> docker-compose run web python /code/manage.py createsuperuser
```

Finally, you can start/stop the server using:
```bash
$> docker-compose up -d --build
$> docker-compose down
```

## Usage
Fetch orders from API:
```bash
$> docker-compose run web python /code/manage.py fetch_orders
```

## Testing
