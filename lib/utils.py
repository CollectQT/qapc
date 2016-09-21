# builtin
import os
import itertools
import collections
import distutils.util
from os import environ as ENV
# external
import bs4
import yaml
import dotenv
import flask_scss
import flask_cache
import flask_misaka


############################################################
# setup
############################################################


dotenv.load_dotenv( dotenv.find_dotenv() )
base_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')

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
# general use functions
############################################################


def read_file(file_name):
    with open(file_name, 'r') as readme_file:
        content = readme_file.read()
    return content

def read_html(table_str):
    soup = bs4.BeautifulSoup(table_str, 'html.parser')
    table_dict = collections.OrderedDict()
    for video in soup.find_all('tr'):
        columns = video.find_all('td')
        name    = columns[4].find('a').contents[0]
        link    = columns[4].find('a').get('href')
        date    = columns[3].contents[0]
        price   = columns[5].contents[0]
        sales   = columns[6].contents[0]
        table_dict[name] = {
            'name': name,
            'date': date,
            'price': price,
            'sales': sales,
            'link': link
        }
    return table_dict

def load_IWC_data():
    path = os.path.join(base_dir, 'data/IWC.txt')
    with open(path, 'r') as table_file:
        table = read_html( table_file.read() )
    return table

def load_shoot_roles():
    path = os.path.join(base_dir, 'data/shoot_roles.yaml')
    with open(path, 'r') as yaml_file:
        shoot_data = yaml.load(yaml_file)
    return shoot_data

def load_role_percents():
    path = os.path.join(base_dir, 'data/role_percents.yaml')
    with open(path, 'r') as yaml_file:
        roles_percents = yaml.load(yaml_file)
    return roles_percents

def get_table():
    '''
    The load_IWC_data function will eventually change.
    When it does, the test for this function should still pass.
    So we use this function as an entry point for getting the IWC data.
    None of the other data files are fetched remotely (yet),
    so they do not need a utils.get_* function.
    '''
    return load_IWC_data()

def load_IWC_images():
    path = os.path.join(base_dir, 'data/IWC_images.yaml')
    with open(path, 'r') as image_file:
        images = yaml.load( image_file.read() )
    return images

def get_images():
    return load_IWC_images()

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
