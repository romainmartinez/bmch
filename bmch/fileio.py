# -*- coding: utf-8 -*-
"""fileio module."""
import pandas as pd  # create_conf_file
import csv  # write_conf_header, create_conf_file
import json  # create_conf_file
import os  # read_c3d_file
import btk  # C3D class
import bmch  # C3D class
import numpy as np  # C3D class


def write_conf_header(metadata_path):
    """Create and write header in the csv configuration files.

    :param metadata_path: path to the metadata folder
    :type metadata_path: str
    Example::

    result = write_conf_header('/home/romain/Downloads/irsst/metadata/')
    """
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
    """Create a json conf file based on the csv conf files.

    :param metadata_path: path to the metadata folder
    :type metadata_path: str
    Example::

    result = write_conf_header('/home/romain/Downloads/irsst/metadata/')
    """
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
    """Load the json configuration file create with the function `create_conf_file`.

    :param metadata_path: path to the metadata folder
    :type metadata_path: str
    Example::

    result = load_conf_file('/home/romain/Downloads/irsst/metadata/')
    """
    json_path = '{}config.json'.format(metadata_path)
    with open(json_path, 'r') as json_data:
        return json.load(json_data)


def save_conf_file(metadata_path, json_file):
    json_path = '{}config.json'.format(metadata_path)
    with open(json_path, 'w') as json_data:
        json_data.write(json.dumps(json_file, indent=4))


class C3D:
    """C3D class read c3d files and return data.

    :param data_folders: dict with path to the data folder(s) as key and type (*markers and/or emg and/or emg*) as value
    :type data_folders: dict

    Example::

        data_folders = {'/home/romain/Downloads/irsst/inputs/DapO/mvc/': ['emg'],
                       '/home/romain/Downloads/irsst/inputs/DapO/score/': ['markers']}
        c3d = load_conf_file(data_folders)
        c3d.read_data()
    """

    def __init__(self, data_folders, conf_file):
        """Constructor for C3D"""
        print('import c3d files from:')
        self.folders = data_folders
        self.conf_file = conf_file
        self.assign = []

    def read_data(self):
        # todo complete return docstring
        """Read data from `self.folders`

        :return
        """
        for ifolder, kind in self.folders.items():
            print('\t{}'.format(ifolder))
            c3d_files = [f for f in os.listdir(ifolder) if f.endswith('.c3d')]
            for ifile in c3d_files:
                print('\t\t{}'.format(ifile))
                file = os.path.join(ifolder, ifile)
                metadata, markers, analogs = self._open_file(file, kind)
        save_assign

    def _open_file(self, file, kind):
        """Open c3d acquisition (*private function*).

        :param file: path to the c3d file
        :type file: str
        :param kind: type (*markers and/or emg and/or emg*)
        :type kind: list
        """
        reader = btk.btkAcquisitionFileReader()
        reader.SetFilename(file)
        reader.Update()
        acq = reader.GetOutput()
        metadata = {'first_frame': acq.GetFirstFrame(), 'last_frame': acq.GetLastFrame()}

        data = {}
        for i in ['markers', 'force', 'emg']:
            if i in kind:
                if i is 'markers':
                    metadata.update({'point_rate': acq.GetPointFrequency(), 'point_used': acq.GetPointNumber()})
                    data_temp = self._iterate(acq=acq, kind='markers')
                    n = metadata['last_frame']
                else:
                    metadata.update({'analog_rate': acq.GetAnalogFrequency(), 'analog_used': acq.GetAnalogNumber()})
                    data_temp = self._iterate(acq=acq, kind='analogs')
                    n = (metadata['last_frame'] * metadata['analog_rate']) / acq.GetPointFrequency()
                data[i] = self._attribute_channels(data_temp, kind=i, frames=n)
            else:
                data[i] = None

    def _attribute_channels(self, data_temp, kind, frames):
        fields = list(data_temp.keys())
        targets = list(self.conf_file[kind]['labels'].values())

        # TODELETE:
        # targets[-1] = 'Voltage.1'

        # gui = bmch.util.GuiC3D(targets, fields)
        gui = ['Delt_ant.EMG1',
               'Delt_med.EMG2',
               'Delt_post.EMG3',
               'Biceps.EMG4',
               'Triceps.EMG5',
               'Trap_sup.EMG6',
               'Pec.IM EMG12',
               'Supra.EMG9',
               'Infra.EMG10']

        output = np.zeros((int(frames), len(targets)))
        for i, iassign in enumerate(gui):
            output[:, i] = np.squeeze(data_temp[iassign])

        itarget = 'Delt_ant.EMG1'

        # check if all target are in fields

        # check if all previous assign are in fields

        # GUI
        gui = bmch.util.GuiC3D(targets, fields)
        self.assign.append(gui.assign)

        # save assign
        return output

    @staticmethod
    def _iterate(acq, kind='markers'):
        """Iterate through a btkCollection object (*private function*) and return data as dict.

        :param acq: btkAcquisition object
        :type acq: btk.btkAcquisition
        :param kind: type of the data (*markers or analogs*)
        :type kind: str
        """
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
