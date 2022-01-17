#!/bin/bash

if ! hash python &> /dev/null
then
    echo "Python not installed!"
    exit
fi

mkdir $HOME/.local/share/barnacle
cp main.py $HOME/.local/share/barnacle
sudo cp barnacle /bin
sudo chmod +x /bin/barnacle