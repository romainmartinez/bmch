# -*- coding: utf-8 -*-
"""Preprocessing submodule."""
# TODO: complete doc
import os


def createproject(project_folder=None):
    # TODO: doc
    # locate project folder
    if project_folder is None:
        project_folder = input('Enter the path of the project: ')
    assert os.path.exists(project_folder), 'the directory {} does not exist'.format(project_folder)
    # TODO: create folder is doesn't exist
    print('directory located')

    # create root folders
    assert not os.listdir(project_folder), 'the directory {} is not empty'.format(project_folder)
    folders = ['inputs', 'outputs', 'metadata']
    [os.mkdir(project_folder + ifolder) for ifolder in folders]
    print('root folders created')

    # create configuration files
    files = ['emg', 'markers', 'force', 'participants', 'trials']


def importproject():
    pass


def importfiles():
    pass
