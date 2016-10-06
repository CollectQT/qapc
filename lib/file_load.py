# builtin
import os
import collections
# external
import bs4
import yaml


############################################################
# setup
############################################################


base_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')


############################################################
# file load functions
############################################################


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


def load_workers():
    path = os.path.join(base_dir, 'data/workers.yaml')
    with open(path, 'r') as yaml_file:
        workers = yaml.load(yaml_file)
    return workers


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

