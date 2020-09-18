create and run docker container named as ```gpu-base```,  init it with command bash
```
docker run -it --gpus all --name gpu-base nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04 bash
```
add following for gui
```
-e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix
```


start the docker with its init command: 
```
docker start gpu-base
```

enter to a running docker container with command bash
```
docker exec -it gpu-base /bin/bash
```
