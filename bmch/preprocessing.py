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
    bmch.fileio.write_conf_header(metadata_path)
    print('\tconfiguration files created')


def import_project(project_path=None):
    # TODO: doc
    # validate path
    project_path, metadata_path = bmch.util.validate_path(project_path, metadata=True)

    # create conf file (json)
    bmch.fileio.create_conf_file(metadata_path)
    print('\tconfiguration files loaded')


def import_files(project_path=None):
    # TODO: doc
    # validate path
    project_path, metadata_path = bmch.util.validate_path(project_path, metadata=True)

    # load conf file
    conf_file = bmch.fileio.load_conf_file(metadata_path)

    # check c3d fields
    import c3d
    path2data = '/home/romain/Downloads/irsst/inputs/IRSST_DapO/trials/DapOF6H1_3.c3d'
    reader = c3d.Reader(open(path2data, 'rb'))
    reader.r


# TODO: delete this
if __name__ == '__main__':
    import_files(project_path='/home/romain/Downloads/irsst')
