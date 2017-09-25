# -*- coding: utf-8 -*-
# TODO: doc
import pandas as pd  # create_conf_file
import csv  # write_conf_header, create_conf_file
import json  # create_conf_file
import c3d  # read_c3d_file
import os  # read_c3d_file


def write_conf_header(metadata_path):
    # TODO: doc
    files = ['emg', 'markers', 'force', 'participants', 'trials']
    headers = {
        'emg': ['labels', 'publication_name'],
        'markers': ['labels'],
        'force': ['labels'],
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
    csv_dict = {ifile: pd.read_csv('{}{}.csv'.format(metadata_path, ifile)) for ifile in files}

    # merge dicts into json files
    json_file = {key: json.loads(csv_dict[key].to_json()) for key in csv_dict}

    # export json file
    json_path = '{}config.json'.format(metadata_path)
    with open(json_path, 'w') as json_data:
        json_data.write(json.dumps(json_file, indent=4))


def load_conf_file(metadata_path):
    # TODO: doc
    json_path = '{}config.json'.format(metadata_path)
    with open(json_path, 'r') as json_data:
        return json.load(json_data)


def read_c3d_file(data_folders):
    # todo: doc
    class C3d:
        def __init__(self, folders, metadata=False, data=False):
            self.folders = folders
            self.flags = [metadata, data]
            # todo: transform to list comprehension:
            for ifolder in folders:
                onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(join(mypath, f))]

        def main(self, metadata=False, data=False):
            output_metadata, output_data = None, None
            with open(file_path, 'rb') as read:
                handler = c3d.Reader(read)
                if metadata:
                    output_metadata = get_metadata(handler)
                if data:
                    output_data = get_data()
            return output_metadata, output_data

    c3d_files = C3d(data_folders)
