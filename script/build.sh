#! /bin/bash

workspaceFolder="$(dirname "$(realpath "$0")")"
cd "$workspaceFolder"

mkdir -p build
cd build

sudo apt install gcc g++ make cmake
sudo apt-get install pkg-config
sudo apt-get install libmagickwand-dev

cmake -DCMAKE_BUILD_TYPE=Release ..
make
