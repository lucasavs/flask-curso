from app import app
from flask import request


@app.route('/name_lastname')
def name_lastname():
    dct = request.args
    name = dct['name']
    lastname = dct['lastname']
    request.args
    return f'{name} {lastname}'
