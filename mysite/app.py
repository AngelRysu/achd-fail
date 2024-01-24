from flask import Flask, render_template, send_from_directory
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

@app.route('/img/<filename>', methods=['GET'])
def route_img_files(filename):
    return send_from_directory('templates/img', path=filename)


@app.route('/css/<filename>')
def route_js_files(filename):
    return send_from_directory('templates/css', path=filename)

@app.route('/js/<filename>')
def route_css_files(filename):
    return send_from_directory('templates/js', path=filename)

@app.route('/')
def hello_world():
    return render_template('index.html')

