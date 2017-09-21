# -*- coding: utf-8 -*-
import os  # validate_path


def validate_path(path, isempty=False, metadata=False):
    # TODO: doc
    # ask project path it is not given
    if path is None:
        path = input('Enter the path of the project: ')

    # add trailing slash if not already here
    project_path = os.path.join(path, '')

    assert os.path.exists(project_path), 'the directory {} does not exist'.format(project_path)

    # raise error if dir is not empty
    if isempty:
        assert not os.listdir(project_path), 'the directory {} is not empty'.format(project_path)

    # return metadata path
    if metadata:
        metadata_path = os.path.join(path, 'metadata', '')
    else:
        metadata_path = None
    return project_path, metadata_path


def create_root_folders(project_path):
    folders = ['inputs', 'outputs', 'metadata']
    [os.mkdir(project_path + ifolder) for ifolder in folders]
