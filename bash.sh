#! /bin/bash

function activate() {
	if [ -z "$1" ]
		then
		    en="/home/"$USER"/venv/venv/bin/activate"
	else
		en="/home/"$USER"/venv/venv_"$1"/bin/activate"
		
	fi
	echo $en
	source $en
}
