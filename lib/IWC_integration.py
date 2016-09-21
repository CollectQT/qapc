# builtin
import os
from os import environ as ENV
# external
import bs4
import dotenv
import splinter
import requests
# local
from lib import utils


############################################################
# setup
############################################################


dotenv.load_dotenv( dotenv.find_dotenv() )
base_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')


############################################################
# functions
############################################################


def wait_for_tag_load(browser, element):
    counter = 0
    while not len(browser.find_by_tag(element)):
        counter += 1
        if counter >= 100: # 10 seconds
            raise Exception('timeout while waiting for \"{}\"'.format(element))
        else:
            time.sleep(0.1)

def login_and_get_table():
    with splinter.Browser('phantomjs') as browser:
        try:
            # login
            browser.driver.set_window_size(1366,768)
            browser.visit('https://iwantclips.com/login/fancy_login')
            wait_for_tag_load(browser, 'form')
            browser.fill('email', ENV['IWC_USER'])
            browser.fill('password', ENV['IWC_PASS'])
            browser.find_by_name('submit').click()
            # get the content table
            browser.visit('https://iwantclips.com/model/content_store')
            wait_for_tag_load(browser, 'tbody')
            content = browser.find_by_tag('tbody')[0].html
            print(content)
            return content
        except Exception as e:
            browser.driver.save_screenshot('error.png')
            raise


def image_from_video_url(url):
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.content, 'html.parser')
    image = soup.find('video').get('poster')
    return image


def get_images_for_videos(table):
    images = {}

    for name, video in table.items():
        images[name] = image_from_video_url(video['link'])

    return images


if __name__ == '__main__':
    table = login_and_get_table()
    path = os.path.join(base_dir, 'data/IWC.txt')
    with open(path, 'w') as data_file:
        data_file.write(table)
