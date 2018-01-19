# -*- coding: utf-8 -*-
import os  # validate_path
import tkinter as tk  # GuiC3D


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


class GuiC3D:
    def __init__(self, targets, fields):
        self.targets = targets
        self.fields = fields

        self.idx = 0
        self.mwheel_count = 0
        self.assign = []
        self.FONTSIZE = 20

        self.init_master()

        self.keyboard()
        self.target()
        self.lists()
        self.buttons()

        self.run()

    def init_master(self):
        self.root = tk.Tk()
        self.root.title('GUI - channels assignment')

    def keyboard(self):
        self.root.bind('1', self.action_add)
        self.root.bind('2', self.action_nan)

    def target(self):
        self.label = tk.Label(self.root, text=self.targets[self.idx], font=(None, self.FONTSIZE))
        self.label.grid(row=0)

    def lists(self):
        self.list_fields = tk.Listbox(self.root, font=(None, self.FONTSIZE))
        self.list_fields.focus_set()
        self.list_fields.insert(0, *self.fields)
        self.list_fields.grid(row=1, column=0, rowspan=7, padx=10)
        self.list_fields.config(height=0)

        self.list_assigned = tk.Listbox(self.root, font=(None, self.FONTSIZE))
        self.list_assigned.grid(row=1, column=2, rowspan=7, padx=10)
        self.list_fields.config(height=0)

    def buttons(self):
        self.button_add = tk.Button(self.root, text='Add [1]', font=(None, self.FONTSIZE),
                                    command=self.action_add)
        self.button_add.grid(row=1, column=1, sticky='W')

        self.button_nan = tk.Button(self.root, text='NaN [2]', font=(None, self.FONTSIZE),
                                    command=self.action_nan)
        self.button_nan.grid(row=2, column=1, sticky='W')

    def action_add(self, event=None):
        selection = self.list_fields.curselection()[0]
        self.list_fields.delete(selection)
        self.list_assigned.insert('end', f'{self.idx}_{self.fields[selection]}')
        self.prepare_next(selection)

    def action_nan(self, event=None):
        selection = self.list_fields.curselection()[0]
        self.list_assigned.insert('end', f'{self.idx}_nan')
        self.prepare_next(selection)

    def prepare_next(self, selection):
        self.list_fields.select_set(selection)
        self.idx += 1
        if self.idx >= len(self.targets):
            self.root.destroy()
        else:
            self.label.config(text=self.targets[self.idx])
            self.assign.append(self.fields[selection])
            del (self.fields[selection])

    def run(self):
        self.root.mainloop()
