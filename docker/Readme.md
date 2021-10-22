Add current user to docker group
```
sudo groupadd docker
sudo gpasswd -a $USER docker
sudo service docker restart
```


create and run docker container named as ```gpu-base```,  init it with command bash
```
docker run -it --gpus all --name gpu-base nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04 bash
```
add following for gui
```
-e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix
-e DISPLAY=$DISPLAY --volume="$HOME/.Xauthority:/root/.Xauthority:rw"
```
ps ```xhost local:root``` on host to enable accessing to xserver

start the docker with its init command: 
```
docker start gpu-base
```

enter to a running docker container with command bash
```
docker exec -it gpu-base /bin/bash
```


success script history
```
xhost +
xhost local:root
```
```
docker run -it --gpus all -e DISPLAY=$DISPLAY --volume="$HOME/.Xauthority:/root/.Xauthority:rw" --net=host -p 5000:5000 --name gpu-base nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04 bash
docker start gpu-base
docker exec -it gpu-base /bin/bash
docker stop gpu-base
docker container rm gpu-base
```


```
docker run -it --volume="/media/$USER/{drive}:/root/{name}:rw" --name {name} ubuntu:focal bash
```
