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


class C3D:
    # todo: doc
    def __init__(self, data_folders, metadata=False, data=False):
        self.folders = data_folders
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
                metadata, data = self.open_file(file, kind)
                # assign c3d fields

    def open_file(self, file, kind):
        with open(file, 'rb') as reader:
            handler = c3d.Reader(reader)
            meta = self.get_metadata(handler) if self.flags['metadata'] else []
            dat = self.get_data(handler, kind) if self.flags['data'] else []
            return meta, dat

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

    @staticmethod
    def get_data(handler, kind):
        points = []
        analogs = []
        kind = str(kind)
        for frame_no, point, analog in handler.read_frames():
            if 'marker' in kind:
                points.append(point)
            if 'emg' in kind:
                analogs.append(analog)
        points = np.vstack(points) if points else []
        analogs = np.vstack(analogs) if analogs else []
        return {'points': points, 'analogs': analogs}


