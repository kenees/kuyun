from .file import file_blue
from .index import index_blue

base_url = '/api/v1'


def init_view(app):
    app.register_blueprint(index_blue, url_prefix='/')
    app.register_blueprint(file_blue, url_prefix=base_url)
