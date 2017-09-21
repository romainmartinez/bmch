# -*- coding: utf-8 -*-
"""Preprocessing submodule."""
# TODO: complete doc
import bmch  # create_project, import_project, import_file


def create_project(project_path=None):
    # TODO: doc
    # validate path
    project_path, metadata_path = bmch.util.validate_path(project_path, isempty=True, metadata=True)
    print('\tdirectory located')

    # create root folders
    bmch.util.create_root_folders(project_path)
    print('\troot folders created')

    # create configuration files
    files = ['emg', 'markers', 'force', 'participants', 'trials']
    [bmch.fileio.write_conf_header(ifile, path=metadata_path) for ifile in files]
    print('\tconfiguration files created')


def import_project(project_path=None):
    # TODO: doc
    # validate path
    project_path, metadata_path = bmch.util.validate_path(project_path, metadata=True)

    # create conf file
    files = ['emg', 'markers', 'force', 'participants', 'trials']
    bmch.fileio.create_conf_file(metadata_path, files)
    print('\tconfiguration files loaded')


def import_files(project_path=None):
    # TODO: doc
    # validate path
    project_path, metadata_path = bmch.util.validate_path(project_path, metadata=True)

    # load conf file


# TODO: delete this
if __name__ == '__main__':
    import_project(project_path='/home/romain/Downloads/irsst')
