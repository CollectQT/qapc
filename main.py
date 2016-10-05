# builtin
import glob
# external
import flask
# local
from lib import utils, view_handlers


############################################################
# setup
############################################################


app = flask.Flask(__name__, static_folder='static', static_url_path='/static', )
cache = utils.setup(app)


############################################################
# views
############################################################


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/contact')
def contact():
    return flask.render_template('document.html', document='content/contact.md')


@app.route('/docs')
def docs():
    return flask.render_template('docs.html')


@app.route('/docs/contract')
def contract():
    return flask.render_template('document.html', document='content/contract.md')


@app.route('/docs/codeofconduct')
def coc():
    return flask.render_template('document.html', document='content/codeofconduct.md')


@app.route('/profile/<worker_key>')
def profile(worker_key):
    return flask.render_template('profile.html', worker=view_handlers.get_user_profile_info(worker_key))


@app.route('/members')
def members():
    return flask.render_template('members.html', workers=view_handlers.get_all_workers())


# @app.route('/sales')
# def sales():
#     return flask.render_template('sales.html', table=view_handlers.get_and_populate_shoot_table())


############################################################
# error pages
############################################################


@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('partials/base.html',
        content='# Error 404\nPage not found'), 404


@app.errorhandler(500)
def server_error(e):
    return flask.render_template('partials/base.html',
        content='# Error 500\nServer error'), 500


############################################################
# dev mode startup
############################################################


if __name__ == '__main__':
    app.run(port = app.config.get("PORT", 5000))
