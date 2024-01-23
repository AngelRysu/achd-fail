from flask import Flask
from flask_orator import Orator
from configparser import ConfigParser
config = ConfigParser()
config.read("config.ini")


DB_HOST = config.get("DB", "DB_HOST")
DB_PASSWORD = config.get("DB", "DB_PASSWORD")

app = Flask(__name__)

DATABASES = {
    'default': 'mysql',
    'mysql': {
        'driver': 'mysql',
        'host': DB_HOST,
        'database': 'horariosWizard$default',
        'user': 'horariosWizard',
        'password': DB_PASSWORD,
        'prefix': '',
        'log_queries': True,
    }
}


app.config['ORATOR_DATABASES'] = DATABASES
db = Orator(app)

@app.route('/')
def hello_world():
    retrieve = db.table ('datos_ejemplo').get().serialize()
    return str(retrieve)

