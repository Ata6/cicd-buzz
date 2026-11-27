import os

from flask import Flask

from buzz import generator

app = Flask(__name__)


@app.route('/')
def generate_buzz():
    page = '<!doctype html><html lang="en"><head><meta charset="utf-8">'
    page += '<title>CI/CD Buzz - Ata6</title></head><body><h1>'
    page += generator.generate_buzz()
    page += '</h1><p>Greetings from Ata6</p></body></html>'
    return page


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
