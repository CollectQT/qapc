# builtin
import os
import sys
# external
import vcr


############################################################
# setup
############################################################


base_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
sys.path.append(base_dir)
from lib import IWC_integration, file_load


############################################################
# functions
############################################################


def test_image_from_video_url():
    table = file_load.get_table()

    for name, video in table.items():
        stripped_name = name.replace(',','').replace(' ','')
        vcr_path = 'test/vcr/test_IWC_integration/video{}.yaml'.format(stripped_name)

        with vcr.use_cassette('test/vcr/test_IWC_integration/video_{}.yaml'.format(stripped_name)):
            image = IWC_integration.image_from_video_url(video['link'])
            assert image[-4:] == '.gif'
