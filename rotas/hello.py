from app import app


@app.route('/')
def hello():
    return 'Ola madruga!'


@app.route('/nome/<name>')
def hello_name(name):
    return f'Ola {name}!'
