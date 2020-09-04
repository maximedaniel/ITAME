# BUILD & RUN

## FROM LOCAL IMAGE

1. run `docker build -t itame .`
2. run `docker run -it -t itame`
2. run `docker run -p 8000:8000 -t itame`

## FROM REMOTE IMAGE

1. run `docker run -p 8000:8000 --name itame tydius/itame`
