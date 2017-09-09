#!/bin/bash -e
set -x

  CONTAINER=$(docker ps | grep 8083 | awk '{print $NF}')

  if [ ! -z "$CONTAINER" ]
  then
    docker stop $(docker ps | grep 8083 | awk '{print $NF}')
    docker rm $(docker ps | grep 8083 | awk '{print $NF}')
  fi

   docker run -p 8083:5000 -d --name python-app-from-ecr 077077460384.dkr.ecr.ap-southeast-2.amazonaws.com/python-app:latest
