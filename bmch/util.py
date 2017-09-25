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


def get_data_folders(project_path, conf_file):
    participants = list(conf_file['participants']['pseudo'].values())
    folders = list(conf_file['trials']['folder'].values())
    output = {}
    emg_folders = list(conf_file['trials']['emg'].values())
    markers_folders = list(conf_file['trials']['markers'].values())
    force_folders = list(conf_file['trials']['force'].values())

    for iparticipant in participants:
        for i, ifolder in enumerate(folders):
            value = []
            key = os.path.join(project_path, iparticipant, ifolder, '')
            if emg_folders[i]:
                value.append('emg')
            if markers_folders[i]:
                value.append('markers')
            if force_folders[i]:
                value.append('force')
            output[key] = value
    return output
