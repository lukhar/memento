from ubuntu:latest

maintainer lukhar <lukasz.har@gmail.com>

# Add mongodb to repositories
run apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
run echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee /etc/apt/sources.list.d/10gen.list

run apt-get update

run apt-get install -y mongodb-org

run apt-get install -y git

run apt-get install -y python3-pip

run mkdir -p /data/db

run pip3 install pybuilder

run ln -sT /usr/bin/pip3 /usr/bin/pip

run mkdir /memento

add . /memento

workdir /memento

run PYTHONPATH=$PYTHONPATH:src/main/python:src/unittest/python

run pyb install_dependencies

run mongod &
