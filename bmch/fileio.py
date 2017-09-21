# -*- coding: utf-8 -*-
# TODO: doc
import pandas as pd  # create_conf_file
import csv  # write_conf_header, create_conf_file
import json  # create_conf_file


def write_conf_header(metadata_path):
    # TODO: doc
    files = ['emg', 'markers', 'force', 'participants', 'trials']
    headers = {
        'emg': ['muscle_id', 'publication_name'],
        'markers': ['marker_id'],
        'force': ['analog_id'],
        'participants': ['pseudo', 'process', 'laterality', 'group', 'mass', 'height', 'date'],
        'trials': ['folder', 'emg', 'markers', 'force']
    }
    for ifile in files:
        with open('{}{}.csv'.format(metadata_path, ifile), 'w') as out:
            writer = csv.DictWriter(out, fieldnames=headers[ifile])
            writer.writeheader()


def create_conf_file(metadata_path):
    # TODO: doc
    files = ['emg', 'markers', 'force', 'participants', 'trials']
    # read each csv files into dict
    d = {name: pd.read_csv('{}{}.csv'.format(metadata_path, name)) for name in files}

    # merge dicts into json files
    z = {k: json.loads(d[k].to_json()) for k in d}

    # export json file
    outpath = '{}config.json'.format(metadata_path)
    with open(outpath, 'w') as out:
        out.write(json.dumps(z, indent=4))
