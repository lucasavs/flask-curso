from flask import Blueprint


from ext.db import db
from blueprints.posts.models import Post

bp = Blueprint('posts', __name__)


def init_app(app, url_prefix='/posts'):
    app.register_blueprint(bp, url_prefix=url_prefix)


@bp.route('/new', methods=['GET', 'POST'])
def new():
    post = Post(title="Meu Post", content="meu conteudo")
    db.session.add(post)
    db.session.commit()
