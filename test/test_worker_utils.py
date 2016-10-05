# builtin
import os
import sys


############################################################
# setup
############################################################


base_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
sys.path.append(base_dir)
from lib import worker_utils


############################################################
# tests
############################################################


def test_init():
    assert 1 == 1

