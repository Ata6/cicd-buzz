import os

from flask import Flask

from buzz import generator

app = Flask(__name__)


@app.route('/')
def generate_buzz():
    page = '<!doctype html><html lang="nl"><head><meta charset="utf-8">'
    page += '<title>Automation - Ata6</title></head><body>'
    page += '<h1>Mijn buzz-generator</h1>'
    page += '<p>Ververs de pagina voor een nieuwe zin.</p><h2>'
    page += generator.generate_buzz()
    page += '</h2><p>Greetings from Ata6</p></body></html>'
    return page


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
