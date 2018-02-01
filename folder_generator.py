import os
import pandas as pd
import settings


def read_json(path):
    with open(path) as fd:
        return pd.read_json(path)


def create_folder(directory):
    try:
        if not os.path.exists('test/'+directory):
            os.makedirs('test/'+directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def generate(json):
    structure = [x for x in read_json(json)[settings.root]]
    items = [child for folder in structure for child in folder]

    for i in (items):
        if 'children' in i:
            for c in i['children']:
                create_folder(str(i['name']) + '/'+  str(c['name']))

    [create_folder(items[i]['name']) for i, folder in enumerate(items) if items[i]['type'] == 'folder']



generate('data/unity.json')
