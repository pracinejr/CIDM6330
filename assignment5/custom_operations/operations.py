from dotenv import load_dotenv
import os
import requests
import sys

load_dotenv(dotenv_path="../.env")

sys.path.append(os.getenv("PYTHONPATH"))
from assignment4.webArchitectures.assignment4.soundBody.models import models
from assignment4.webArchitectures.assignment4.assignment4.api import api
