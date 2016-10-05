# builtin
import os
import sys
import pprint


############################################################
# setup
############################################################


# http://flask.pocoo.org/docs/0.11/testing/

base_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
sys.path.append(base_dir)
from main import app


def content_on_page(route, content='Queer Art and Porn Collective'):
    # essentially just testing that the page builds at all
    client  = app.test_client()
    page    = client.get(route)
    data    = str(page.data)
    pprint.pprint(data)
    return content in data


############################################################
# tests
############################################################


def test_true(): assert True


def test_index():
    assert content_on_page('/')


def test_contact():
    assert content_on_page('/contact', 'qapcollective@gmail.com')


def test_cyrin_profile():
    assert content_on_page('/profile/Cyrin', 'Cyrin Song')


def test_docs():
    assert content_on_page('/docs', 'Documents')


def test_coc():
    assert content_on_page('/docs/codeofconduct', 'Code of Conduct')


def test_contract():
    assert content_on_page('/docs/contract', 'Contract')

