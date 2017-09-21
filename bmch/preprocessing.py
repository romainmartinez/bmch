# -*- coding: utf-8 -*-
"""Preprocessing submodule."""
# TODO: complete doc
import bmch
import os


def create_project(project_path=None):
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
    [bmch.fileio.write_conf_header(ifile, path=metadata_path) for ifile in files]
    print('\tconfiguration files created')


def import_project(project_path=None):
    # TODO: doc
    # validate path
    project_path = bmch.util.validate_path(project_path)

    # create conf file
    metadata_path = os.path.join(project_path, 'metadata', '')
    files = ['emg', 'markers', 'force', 'participants', 'trials']
    bmch.fileio.create_conf_file(metadata_path, files)
    print('\tconfiguration files loaded')


def import_files(project_path=None):
    # TODO: doc
    # validate path
    project_path = bmch.util.validate_path(project_path)

    # load conf file


# TODO: delete this
if __name__ == '__main__':
    import_project(project_path='/home/romain/Downloads/irsst')
