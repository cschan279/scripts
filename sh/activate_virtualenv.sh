#! /bin/bash

# copy it into .bashrc
function activate() {
  if [ -z "$1" ]
    then
      en="/home/"$USER"/venv/venv/bin/activate"
  else
    en="/home/"$USER"/venv/"$1"/bin/activate"
  fi
  echo $en
  source $en
}

function tfcheckgpu() {
    python -c "import tensorflow as tf;print(tf.config.list_physical_devices('GPU'));"
}
