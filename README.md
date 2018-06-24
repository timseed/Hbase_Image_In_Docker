
# Hbase Photo server1

To build the project from scratch you need to do a

    docker-compose build
    docker-compose up


Then using **docker exec** connect to the hbase-container, and for the moment, create some data.

This is what you need to type


```bash
hbase shell
create 'people','cf'
put 'people',"1",'cf:name1:','tim'
put 'people',"2",'cf:name1:','juliet'
put 'people',"2",'cf:name2:','dora'
exit
```

You can stop and start the container - and the data will persist (as there is a Volume called hbdata). If you want to delete ALL Your data - you can rm that volume, build and up.
