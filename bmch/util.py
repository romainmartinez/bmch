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
