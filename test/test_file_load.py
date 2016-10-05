# builtin
import os
import sys
import collections


############################################################
# setup
############################################################


base_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
sys.path.append(base_dir)
from lib import file_load


############################################################
# tests
############################################################


def test_true(): assert True


def test_load_shoot_roles():
    data = file_load.load_shoot_roles()
    assert isinstance(data['Ali3n Club Fuck']['Workers'], dict)


def test_load_role_percents():
    data = file_load.load_role_percents()
    assert 0 <= data['Performer'] <= 100
    assert 0 <= data['QAPC'] <= 100


def test_load_workers():
    data = file_load.load_workers()
    assert isinstance(data, dict)
    assert bool(data)


def test_get_table():
    data = file_load.get_table()
    assert isinstance(data, collections.OrderedDict)
    assert bool(data)


def test_get_images():
    data = file_load.get_images()
    assert isinstance(data, dict)
    assert bool(data)


def test_get_first_video_from_table():
    video = list(file_load.get_table().items())[0][1]
    assert isinstance(video, dict)
    assert bool(video)
