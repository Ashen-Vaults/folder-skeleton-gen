#!/usr/bin/env python

import os
import pandas as pd
import settings


def get_json(path):
    with open(path) as fd:
        return [x for x in pd.read_json(path)[settings.root]]


def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(''+directory)
    except OSError:
        print('Error: Creating directory. ' + directory)
    return directory


def generate(json):
    structure = get_json(json)
    items = [x for folder in structure for x in folder]
    [create_folder(items[i]['name']) for i, folder in enumerate(items) if items[i]['type'] == 'folder']
    [create_folder(str(i['name']) + '/' + str(c['name'])) for i in items if 'children' in i for c in i['children']]

generate('data/unity.json')
