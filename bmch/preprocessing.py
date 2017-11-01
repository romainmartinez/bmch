# -*- coding: utf-8 -*-
"""Preprocessing submodule."""
import bmch  # create_project, import_project, import_file


def create_project(project_path=None):
    """Create root folders (*inputs, outputs and metadata*) and csv configuration files. You must fill these files.

    :param project_path: path to the project
    :type: str
    """
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
    """Import csv configurations files created by `create_project` and create a json configuration file.

    :param project_path: path to the project
    """
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

    # get data folders
    data_folders = bmch.util.get_data_folders(project_path, conf_file)

    # read c3d files
    c3d = bmch.fileio.C3D(data_folders)
    c3d.read_data()


if __name__ == '__main__':
    import_files(project_path='/home/romain/Downloads/irsst')
    pass
