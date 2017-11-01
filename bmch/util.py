# -*- coding: utf-8 -*-
import os  # validate_path


def validate_path(path, isempty=False, metadata=False):
    """Check if the path exist. If a path is not provided, ask the user to type one.

    :param path: path to validata
    :type path: str
    :param isempty: check if the folder is empty if True
    :type isempty: bool
    :param metadata: return also the metadata path if True
    :return: path validated and metadata path if `metadata=True`
    Example::

    project_path, metadata_path = validate_path(project_path='/home/romain/Downloads/irsst',
                                                isempty=True, metadata=True)
    """
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
    """Create the root folders of the project (*inputs, ouputs and metadata*)

    :param project_path: path to the project
    :type project_path: str
    """
    folders = ['inputs', 'outputs', 'metadata']
    [os.mkdir(project_path + ifolder) for ifolder in folders]


def get_data_folders(project_path, conf_file):
    """Get data folders and associated type (*markers and/or emg and/or emg*).

    :param project_path: path to the project
    :type project_path: str
    :param conf_file: json conf file load as dict
    :type conf_file: dict
    :return: output: dict containing the data folder(s) as key and type (*markers and/or emg and/or emg*) as value
    """
    participants = list(conf_file['participants']['pseudo'].values())
    blacklist = list(conf_file['participants']['process'].values())
    folders = list(conf_file['trials']['folder'].values())

    output = {}
    emg_folders = list(conf_file['trials']['emg'].values())
    markers_folders = list(conf_file['trials']['markers'].values())
    force_folders = list(conf_file['trials']['force'].values())

    for b, iparticipant in enumerate(participants):
        if blacklist[b]:
            for i, ifolder in enumerate(folders):
                value = []
                key = os.path.join(project_path, 'inputs', iparticipant, ifolder, '')
                if emg_folders[i]:
                    value.append('emg')
                if markers_folders[i]:
                    value.append('markers')
                if force_folders[i]:
                    value.append('force')
                output[key] = value
    return output
