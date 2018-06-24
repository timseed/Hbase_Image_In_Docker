
# Hbase Photo Server in Docker

To build the project from scratch you need to do a

    docker-compose build
    docker-compose up -d


Then using **docker exec** connect to the hbase-container, and for the moment, create some data.

This is what you need to type


```bash
hbase shell
create 'photo','cf'
exit
```

You can stop and start the container - and the data will persist (as there is a Volume called hbdata). If you want to delete ALL Your data - you can rm that volume, build and up.

# Containers are running

When the containers are running you now can go into the non-docker folder, where you should find some jpg and some py files.

## Python Env Requirements

Your python3 env needs to have the following modules loaded

  - happybase

## Testing setup

To test everything is working you should run some of the python files.

  - check_hbase.py
  - check_uu.py

Assuming that these work, then you can load some test images in using the python script called **load_hbase.py**. This does 99% of what would be needed in a full production non-duplicate image loading scenario.

# WebSrv Container

This is currently Work in Progress..... but stay tuned.