import os
from flask import request, json, Response
from flask_api import FlaskAPI
from flask_cors import CORS

APP = FlaskAPI(__name__)
CORS(APP)

STATUS = "STATUS"
ERROR_FILES_LIST = "ERROR_FILES_LIST"