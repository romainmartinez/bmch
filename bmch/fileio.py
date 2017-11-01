# -*- coding: utf-8 -*-
# TODO: doc
import pandas as pd  # create_conf_file
import csv  # write_conf_header, create_conf_file
import json  # create_conf_file
import os  # read_c3d_file
import btk  # C3D class


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
    def __init__(self, data_folders):
        print('import c3d files from:')
        self.folders = data_folders

    def read_data(self):
        for ifolder, kind in self.folders.items():
            print('\t{}'.format(ifolder))
            c3d_files = [f for f in os.listdir(ifolder) if f.endswith('.c3d')]
            for ifile in c3d_files:
                print('\t\t{}'.format(ifile))
                file = os.path.join(ifolder, ifile)
                metadata, markers, analogs = self._open_file(file, kind)

    def _open_file(self, file, kind):
        reader = btk.btkAcquisitionFileReader()
        reader.SetFilename(file)
        reader.Update()
        acq = reader.GetOutput()
        metadata = {'first_frame': acq.GetFirstFrame(), 'last_frame': acq.GetLastFrame()}
        if 'markers' in kind:
            metadata.update({'point_rate': acq.GetPointFrequency(), 'point_used': acq.GetPointNumber()})
            markers = self._iterate(acq=acq, kind='analogs')
        else:
            markers = None
        if 'force' in kind or 'emg' in kind:
            metadata.update({'analog_rate': acq.GetAnalogFrequency(), 'analog_used': acq.GetAnalogNumber()})
            analogs = self._iterate(acq=acq, kind='analogs')
        else:
            analogs = None
        return metadata, markers, analogs

    @staticmethod
    def _iterate(acq, kind='markers'):
        out = {}
        if kind == 'markers':
            iterator = btk.Iterate(acq.GetPoints())
        elif kind == 'analogs':
            iterator = btk.Iterate(acq.GetAnalogs())
        else:
            iterator = []
        for it in iterator:
            data_temp = it.GetValues()
            if data_temp.any():
                out.update({it.GetLabel(): data_temp})
        return out
