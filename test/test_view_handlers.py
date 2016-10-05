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


def test_init():
    assert 1 == 1


def test_view_handler():
    table = view_handlers.get_and_populate_shoot_table()
    for video in table.values():
        total_earnings = video['total earnings']
        sum_all_earnings = 0
        for earning in video['earnings'].values():
            sum_all_earnings += earning

        assert round(total_earnings, 2) == round(sum_all_earnings, 2)
        assert video.get('image') is not None
