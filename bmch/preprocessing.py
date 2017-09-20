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
    # validate path
    project_path = bmch.util.validate_path(project_path)

    # create hdf5 file and put metadata
    files = ['emg', 'markers', 'force', 'participants', 'trials']
    bmch.fileio.create_file(project_path)

    for ifile in files:
        # import csv files
        metadata = pd.read_csv('{}/metadata/{}.csv'.format(project_path, ifile))
        # append in hdf5 file
        bmch.fileio.append_metadata(project_path, metadata, ifile)
    print('\tconfiguration files loaded')

    # export cache (project folder only)
    # TODO: see if delete if really necessary


def importfiles(project_path=None):
    # TODO: doc
    # validate path
    project_path = bmch.util.validate_path(project_path)


# TODO: delete this
if __name__ == '__main__':
    importproject(project_path='/home/romain/Downloads/irsst')
