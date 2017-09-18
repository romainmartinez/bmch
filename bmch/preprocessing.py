# -*- coding: utf-8 -*-
"""Preprocessing submodule."""
# TODO: complete doc
import os
import bmch


def createproject(project_path=None):
    # TODO: doc
    # locate project folder
    if project_path is None:
        project_path = input('Enter the path of the project: ')
    project_path = os.path.join(project_path, '')  # add trailing slash if not already here
    assert os.path.exists(project_path), 'the directory {} does not exist'.format(project_path)
    print('\tdirectory located')

    # create root folders
    assert not os.listdir(project_path), 'the directory {} is not empty'.format(project_path)
    folders = ['inputs', 'outputs', 'metadata']
    [os.mkdir(project_path + ifolder) for ifolder in folders]
    print('\troot folders created')

    # create configuration files
    metadata_path = os.path.join(project_path, 'metadata', '')
    files = ['emg', 'markers', 'force', 'participants', 'trials']
    [bmch.util.metaheader(ifile, path=metadata_path) for ifile in files]
    print('\tconfiguration files created')


def importproject(project_path):
    import pandas as pd
    pd.options
    # import conf files (csv)
    files = ['emg', 'markers', 'force', 'participants', 'trials']

    # export single conf file

    # export cache (project folder only)
    pass


def importfiles():
    pass


# TODO: delete this
if __name__ == '__main__':
    createproject(project_path='/home/romain/Downloads/irsst')
