from flask import Blueprint, request

bp = Blueprint('names', __name__)


@bp.route('/name_lastname')
def name_lastname():
    dct = request.args
    name = dct['name']
    lastname = dct['lastname']
    request.args
    return f'{name} {lastname}'


@bp.route('/')
def hello():
    return 'Ola madruga!'


@bp.route('/nome/<name>')
def hello_name(name):
    return f'Ola {name}!'
