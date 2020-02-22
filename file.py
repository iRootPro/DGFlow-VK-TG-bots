import json
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_SETTINGS_FILENAME = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')


def get_phrases(filname):
    with open(filname, 'r') as file:
        questions = json.load(file)
        return questions


def get_project_id():
    with open(GOOGLE_SETTINGS_FILENAME) as file:
        settings = json.load(file)
    project_id = settings['project_id']
    return project_id
