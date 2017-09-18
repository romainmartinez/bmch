# -*- coding: utf-8 -*-


def metaheader(case, path=None):
    # TODO: doc
    import csv
    headers = {
        'emg': ['muscle_id', 'publication_name'],
        'markers': ['marker_id'],
        'force': ['analog_id'],
        'participants': ['pseudo', 'process', 'laterality', 'group', 'mass', 'height', 'date'],
        'trials': ['folder', 'emg', 'markers', 'force']
    }
    # TODO: add headers
    with open(path + case + '.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers[case])
        writer.writeheader()
