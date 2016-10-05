# builtin
import os
import sys


############################################################
# setup
############################################################


base_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
sys.path.append(base_dir)
from lib import file_load, worker_utils, view_handlers


############################################################
# tests
############################################################


def test_true(): assert True


def test_make_worker_video_list():

    workers = file_load.load_workers()
    table = view_handlers.get_and_populate_shoot_table()

    workers = worker_utils.make_worker_video_list(workers, table)

    assert bool(workers)
    assert len( workers['Cyrin']['videos']) >= 1


def test_make_worker_total_earnings():

    workers = file_load.load_workers()
    table = view_handlers.get_and_populate_shoot_table()
    workers = worker_utils.make_worker_video_list(workers, table)

    workers = worker_utils.make_worker_total_earnings(workers)

    assert bool(workers)
    assert 0 <= workers['Cyrin']['earnings']
    assert 0 <= workers['Cyrin']['earnings_map']['Ali3n Club Fuck']
