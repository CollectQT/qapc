# builtin
import itertools
import distutils.util
from os import environ as ENV
# external
import yaml
import dotenv
import flask_scss
import flask_cache
import flask_misaka


############################################################
# setup
############################################################


dotenv.load_dotenv( dotenv.find_dotenv() )


def setup(app):
    # public configs, from config.yaml
    with open('config.yaml','r') as config_file:
        app.config.update( yaml.load( config_file ) )

    app.config['DEBUG'] = distutils.util.strtobool(ENV.get('DEBUG', False))

    # extensions
    flask_misaka.Misaka(app)
    flask_scss.Scss(app, static_dir='static', asset_dir='static')
    cache = flask_cache.Cache(app, config={'CACHE_TYPE': 'simple'})

    return cache


############################################################
# table transforms
############################################################


def video_add_worker_and_roles(video, shoot_roles):
    video['Workers'] = shoot_roles[video['name']]['Workers']
    return video


def video_add_role_unscaled_percents(video, role_percents):
    video['role percents unscaled'] = role_percents
    return video


def video_create_scaling_factor(video):
    total_percent = 0
    total_percent += int(video['role percents unscaled']['QAPC'])

    role_tally = list(itertools.chain.from_iterable(
        video['Workers'].values()
    ))

    for role in role_tally:
        total_percent += int(video['role percents unscaled'][role])

    scaling_factor = 100 / total_percent
    video['scaling factor'] = scaling_factor
    return video


def video_scale_role_percents(video):
    video['role percents'] = {}
    for worker, roles in video['Workers'].items():
        percent = 0
        for role in roles:
            unscaled_percent = int(video['role percents unscaled'][role])
            percent += unscaled_percent * video['scaling factor']
        video['role percents'][worker] = percent
    unscaled_percent = int(video['role percents unscaled']['QAPC'])
    video['role percents']['QAPC'] = unscaled_percent * video['scaling factor']
    return video


def video_get_total_earnings(video):
    price = float(video['price'].strip('$'))
    sales = int(video['sales'])
    IWC_payout = float(0.7)
    video['total earnings'] = price * sales * IWC_payout
    return video


def video_get_worker_earnings(video):
    video['earnings'] = {}
    for worker, percent in video['role percents'].items():
        earnings = video['total earnings'] * percent / 100
        video['earnings'][worker] = earnings
    return video


def video_add_images(video, images):
    video['image'] = images[ video['name'] ]
    return video
