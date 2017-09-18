# -*- coding: utf-8 -*-


def validate_path(path, isempty=False):
    # TODO: doc
    import os
    if path is None:
        path = input('Enter the path of the project: ')
    output_path = os.path.join(path, '')  # add trailing slash if not already here

    assert os.path.exists(output_path), 'the directory {} does not exist'.format(output_path)

    # raise error if dir is not empty
    if isempty:
        assert not os.listdir(output_path), 'the directory {} is not empty'.format(output_path)

    return output_path


def conf_header(case, path=None):
    # TODO: doc
    import csv
    headers = {
        'emg': ['muscle_id', 'publication_name'],
        'markers': ['marker_id'],
        'force': ['analog_id'],
        'participants': ['pseudo', 'process', 'laterality', 'group', 'mass', 'height', 'date'],
        'trials': ['folder', 'emg', 'markers', 'force']
    }
    with open(path + case + '.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers[case])
        writer.writeheader()
