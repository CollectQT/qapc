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


def page_contains_content(route, content='Queer Art and Porn Collective'):
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
    assert page_contains_content('/')


def test_contact():
    assert page_contains_content('/contact', 'qapcollective@gmail.com')


def test_cyrin_profile():
    assert page_contains_content('/profile/Cyrin', 'Cyrin Song')


def test_docs():
    assert page_contains_content('/docs', 'Documents')


def test_coc():
    assert page_contains_content('/docs/codeofconduct', 'Code of Conduct')


def test_contract():
    assert page_contains_content('/docs/contract', 'Contract')

