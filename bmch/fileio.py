# -*- coding: utf-8 -*-
# TODO: doc
import pandas as pd  # create_conf_file
import csv  # write_conf_header, create_conf_file
import json  # create_conf_file
import c3d  # read_c3d_file
import os  # read_c3d_file
import numpy as np  # get_data


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


def read_c3d_file(data_folders, metadata=False, data=False):
    # todo: doc
    class C3d:
        def __init__(self, folders, metadata=False, data=False):
            self.folders = folders
            self.flags = {'metadata': metadata, 'data': data}
            self.current = {}
            print('import c3d files from:')
            self.mainloop()

        def mainloop(self):
            for ifolder, kind in self.folders.items():
                print('\t{}'.format(ifolder))
                c3d_files = [f for f in os.listdir(ifolder) if f.endswith('.c3d')]
                for ifile in c3d_files:
                    print('\t\t{}'.format(ifile))
                    file = ifolder + ifile
                    self.open_file(file, kind)

        def open_file(self, file, kind):
            with open(file, 'rb') as reader:
                handler = c3d.Reader(reader)
                if self.flags['metadata']:
                    self.current['metadata'] = self.get_metadata(handler)
                if self.flags['data']:
                    self.current['data'] = self.get_data(handler, kind)

        @staticmethod
        def get_metadata(handler):
            output = {
                'first_frame': handler.first_frame(),
                'last_frame': handler.last_frame(),

                'point_rate': handler.point_rate,
                'analog_rate': handler.analog_rate,

                'point_used': handler.point_used,
                'analog_used': handler.analog_used,
            }
            if output['point_used'] is not 0:
                output['point_labels'] = handler.groups['POINT'].params['LABELS'].string_array
            if output['analog_used'] is not 0:
                output['analog_labels'] = handler.groups['ANALOG'].params['LABELS'].string_array
            return output

        def get_data(self, handler, kind):
            points = []
            analogs = []
            for frame_no, point, analog in handler.read_frames():
                if point.any():
                    points.append(point)
                if analog.any():
                    analogs.append(analog)
            return 1

    coucou = C3d(data_folders, metadata, data)
