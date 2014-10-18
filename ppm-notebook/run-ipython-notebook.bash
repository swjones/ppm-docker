#!/bin/bash                                                                     
export PYTHONPATH=/home/ppm

IPN_URL="https://github.com/swjones/ppmnotebooks.git"
IPN_LOCAL="/home/ppm/ppmnotebooks"
IPN_DIR="${IPN_LOCAL}/notebooks"

[[ -d ${IPN_DIR} ]] || git clone ${IPN_URL} ${IPN_LOCAL}

ipython notebook \
    --profile=nbserver \
    --pylab=inline \
    --no-browser \
    --ip=0.0.0.0 \
    --port=8080 \
    --notebook-dir=${IPN_DIR}

