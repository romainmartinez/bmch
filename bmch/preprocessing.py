# -*- coding: utf-8 -*-
"""Preprocessing submodule."""
# TODO: complete doc
import bmch
import os


def createproject(project_path=None):
    # TODO: doc
    # validate path
    project_path = bmch.util.validate_path(project_path, isempty=True)
    print('\tdirectory located')

    # create root folders
    folders = ['inputs', 'outputs', 'metadata']
    [os.mkdir(project_path + ifolder) for ifolder in folders]
    print('\troot folders created')

    # create configuration files
    metadata_path = os.path.join(project_path, 'metadata', '')
    files = ['emg', 'markers', 'force', 'participants', 'trials']
    [bmch.util.conf_header(ifile, path=metadata_path) for ifile in files]
    print('\tconfiguration files created')


def importproject(project_path=None):
    # TODO: doc
    import pandas as pd

    project_path = bmch.util.validate_path(project_path, isempty=False)

    files = ['emg', 'markers', 'force', 'participants', 'trials']
    metadata_path = os.path.join(project_path, 'metadata', '')

    # import conf files (csv)
    metadata = {}
    for ifile in files:
        metadata[ifile] = pd.read_csv(metadata_path + ifile + '.csv')
    print('\tconfiguration files loaded')

    # export single conf file

    # export cache (project folder only)
    pass


def importfiles():
    pass


# TODO: delete this
if __name__ == '__main__':
    importproject(project_path='/home/romain/Downloads/irsst')
