from flask import Flask
from flask_orator import Orator


app = Flask(__name__)

DATABASES = {
    'default': 'mysql',
    'mysql': {
        'driver': 'mysql',
        'host': 'horariosWizard.mysql.pythonanywhere-services.com',
        'database': 'horariosWizard$default',
        'user': 'horariosWizard',
        'password': 'Kjkszpj783!A',
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

