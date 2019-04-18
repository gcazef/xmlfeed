# XMLFeed
XML product feed parser for Lengow Test API

## Requirements
 - docker
 - docker-compose
 - GNU Make

## Getting started
The API url can be changed in settings, under ```ORDER_API_URL```.

First, build and initialize the docker image:
```bash
$> make install
```

And run the database and server:
```bash
$> make run
```

To run in background use:
```bash
$> make run_bg
```

## Usage
To fetch orders from the API:
```bash
$> make fetch_orders
```

## Testing
Run the tests with:
```bash
$> make run
```