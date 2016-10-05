# builtin
import os
import sys


############################################################
# setup
############################################################


# http://flask.pocoo.org/docs/0.11/testing/

base_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
sys.path.append(base_dir)
from main import app


############################################################
# tests
############################################################


def test_true(): assert True


def test_index_title():
    client = app.test_client()
    page = client.get('/')

    assert b'Queer Art and Porn Collective' in page.data
