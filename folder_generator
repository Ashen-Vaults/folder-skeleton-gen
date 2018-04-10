#!/usr/bin/env python

import os
import pandas as pd
import settings


def get_json(path):
    '''Returns the json data as data frame'''
    with open(path) as fd:
        return [x for x in pd.read_json(path)[settings.root]]


def create_folder(path):
    path = os.getcwd() +'/'+ path
    '''Attempts to create a folder at specified path
    Returns success. TODO: store fails, and allow for
    re-attempt
    '''
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            return True
    except OSError:
        print('Error: Creating directory. ' + path)
        return False


def parse(json):
    '''Returns the folders we want from json'''
    structure = get_json(json)
    return [x for folder in structure for x in folder]


def generate_parents(items):
    '''Creates top level folders'''
    [create_folder(items[i]['name']) for i, folder in enumerate(items) if items[i]['type'] == 'folder']


def generate_children(items):
    ''' Creates children folders, if any exist '''
    [create_folder(str(i['name']) + '/' + str(c['name'])) for i in items if 'children' in i for c in i['children']]


def generate(file):
    '''Takes in path to json and creates folders'''
    items = parse(file)
    generate_parents(items)
    generate_children(items)


generate('data/unity.json')
