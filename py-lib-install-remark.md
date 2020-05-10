# Install CUDA & CUDNN

> Even pull docker image with tf-gpu,  
> necessary to install cuda with run-file from nvidia  
> since its cuda libs are not complete  
## p.s.
> instead of pull tf-gpu image, 
> it is much better to pull cuda image from nvidia:  
```docker pull nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04```

then install cudnn from tar.gz file  
>   
```
ln -s /usr/local/cuda-10.0/include/cudnn.h /usr/local/include/cudnn.h
ln -s /usr/local/cuda-10.0/lib64/libcudnn.so /usr/local/lib/libcudnn.so
```  
```
ln -s /usr/include/cudnn.h /usr/local/include/cudnn.h
ln -s /usr/lib/x86_64-linux-gnu/libcudnn.so /usr/local/lib/libcudnn.so
```
---

---
# Verify with tensorflow-gpu
> For tf-1.x:
```import tensorflow as tf;tf.test.is_gpu_available();```
> for tf-2.x:
```import tensorflow as tf;tf.config.list_physical_devices('GPU');```
---

---

# dlib with CUDA
### 1. introduction
> if above item lib were installed correctly,  
> install cmake via pip3 install cmake  
> then pip3 install dlib,  
> `sudo` may required to get cuda available in some cases  
### 2. verify
> run  
```python3 -c "import dlib; print(dlib.DLIB_USE_CUDA);"```
---

---

# Compile, install opencv with cuda
### 1. install library
```
apt-get install -y opencv-data &&
apt-get install -y libopencv-dev
```
### 2. enable tesseract build (Optional)
```apt-get install -y tesseract-ocr libtesseract-dev libleptonica-dev```  
### 3. enable gstreamer build (Optional)
```
apt-get install -y gstreamer1.0*
apt install -y ubuntu-restricted-extras
apt install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
```
### 4. pull opencv source code from git and checkout required version
```
ver=4.3.0
wget -O opencv.zip https://github.com/opencv/opencv/archive/$(ver).zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/$(ver).zip
unzip opencv.zip
unzip opencv_contrib.zip
mv opencv* opencv
mv opencv_contrib* opencv_contrib
```
or  
```
ver=4.3.0
git clone https://github.com/opencv/opencv_contrib.git
cd opencv_contrib && git checkout $ver && cd ..
git clone https://github.com/opencv/opencv.git
cd opencv && git checkout $ver
```
### 5. cmake for prepare build
```
mkdir build && cd build

cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D WITH_CUDA=ON \
    -D ENABLE_FAST_MATH=1 \
    -D CUDA_FAST_MATH=1 \
    -D WITH_CUBLAS=1 \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
    -D BUILD_EXAMPLES=ON ..
```
### 6. compile library (It take Time)
check cpu core on the machine with ```nproc```:  
```make -j $(($(nproc) - 1))```
### 7. install library
>   
```sudo make install```  
```sudo ldconfig```

---

---