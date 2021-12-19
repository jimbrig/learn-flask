#!/usr/bin/env bash

mkdir ./flask-appbuilder && cd flask-appbuilder || exit
python3 -m venv venv

source ./venv/bin/activate

pip3 install --upgrade pip
pip3 install Flask Flask-AppBuilder
pip3 freeze > requirements.txt
flask fab create-app --name flaskapp --engine SQLAlchemy