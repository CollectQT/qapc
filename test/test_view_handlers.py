# builtin
import os
import sys
import collections


############################################################
# setup
############################################################


base_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
sys.path.append(base_dir)
from lib import view_handlers


############################################################
# tests
############################################################


def test_true(): assert True


def test_get_and_populate_shoot_table():
    table = view_handlers.get_and_populate_shoot_table()

    assert bool(table)
    assert isinstance(table, collections.OrderedDict)


def test_get_user_profile_info():
    worker = view_handlers.get_user_profile_info('Cyrin')

    assert bool(worker)
    assert 0 <= worker['earnings']
