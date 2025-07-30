#!/bin/bash
NAME=backend
DIR=$(dirname "$(readlink -f "$0")")
WORKERS=3
WORKER_CLASS=uvicorn.workers.UvicornWorker
VENV=$DIR/venv/bin/activate
BIND=0.0.0.0:8003
LOG_LEVEL=info

cd $DIR
source $VENV
source .env

exec gunicorn main:app \
   --name $NAME \
   --workers $WORKERS \
   --worker-class $WORKER_CLASS \
   --bind=$BIND \
   --log-level=$LOG_LEVEL
