from os.path import exists
from shutil import rmtree


def after_all(context):
    path = './tmp'
    if exists(path):
        rmtree(path)
