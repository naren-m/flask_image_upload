#!/usr/bin/env bash

set -e

BUILD_TYPE="${BUILD_TYPE:-dev}"         # dev or prod

if [ ${BUILD_TYPE} == "dev" ];
then
    MAP_VOLUME="-v ${PWD}:/webapp"
    echo ${MAP_VOLUME}
fi

 docker run -d --name flask ${MAP_VOLUME} \
            -p 5000:5000 narenm/flask:py3