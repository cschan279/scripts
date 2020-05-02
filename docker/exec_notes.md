create and run docker container named as ```gpu-base```,  init it with command bash
```
docker run -it --gpus all --name gpu-base tensorflow/tensorflow:latest-gpu-py3 bash
```

start the docker with its init command: 
```
docker start gpu-base
```

enter to a running docker container with command bash
```
docker exec -it gpu-base /bin/bash
```
