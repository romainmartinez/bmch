import tkinter
import bmch


# todo: comments code & doc


class Assignc3d:
    def __init__(self, master, targets, fields):
        self.targets = targets
        self.fields = fields
        self.idx = 0
        self.assign = []

        self.master = master
        master.title('GUI - fields assignment')
        fontsize = 20
        self.current = tkinter.StringVar()
        master.bind('1', lambda event: self.add(event, caller='add'))
        master.bind('2', lambda event: self.add(event, caller='nan'))
        master.bind('3', self.reset)

        self.label = tkinter.Label(master, text=self.targets[self.idx], font=(None, fontsize))
        self.label.grid(row=0)

        self.fields_list = tkinter.Listbox(master, font=(None, fontsize))
        self.fields_list.insert(0, *self.fields)
        self.fields_list.grid(row=1, column=0, rowspan=7)

        self.add_button = tkinter.Button(master, text="Add [1]", font=(None, fontsize),
                                         command=lambda: self.add(caller='add'))
        self.add_button.grid(row=1, column=1, sticky='W')

        self.nan_button = tkinter.Button(master, text="Nan [2]", font=(None, fontsize),
                                         command=lambda: self.add(caller='nan'))
        self.nan_button.grid(row=2, column=1, sticky='W')

        self.reset_button = tkinter.Button(master, text="Reset [3]", font=(None, fontsize),
                                           command=self.reset)
        self.reset_button.grid(row=3, column=1, sticky='W')

        self.points_radio = tkinter.Radiobutton(master, text='markers', font=(None, fontsize),
                                                variable=self.current, value='markers')
        self.points_radio.grid(row=4, column=1, sticky='W')

        self.emg_radio = tkinter.Radiobutton(master, text='emg', font=(None, fontsize),
                                             variable=self.current, value='emg')
        self.emg_radio.grid(row=5, column=1, sticky='W')

        self.force_radio = tkinter.Radiobutton(master, text='force', font=(None, fontsize),
                                               variable=self.current, value='force')
        self.force_radio.grid(row=6, column=1, sticky='W')

        self.assign_list = tkinter.Listbox(master, font=(None, fontsize))
        self.assign_list.grid(row=1, column=2, rowspan=7)

    def add(self, event=None, caller=None):
        selection = self.fields_list.curselection()[0]
        if caller is 'add':
            self.fields_list.delete(selection)
            self.assign_list.insert(0, self.fields[selection])
            del (self.fields[selection])
        elif caller is 'nan':
            self.assign_list.insert(0, 'nan')
        else:
            raise ValueError('Wrong caller')
        self.fields_list.select_set(selection)
        self.idx += 1
        if self.idx >= len(self.targets):
            self.master.quit()
        else:
            self.label.config(text=self.targets[self.idx])
            self.assign.append(self.fields[selection])

    def reset(self, event=None):
        pass


metadata_path = '/home/romain/Downloads/irsst/metadata/'
conf = bmch.fileio.load_conf_file(metadata_path)
target_c3d = list(conf['emg']['labels'].values())
fields_c3d = list(conf['emg']['labels'].values())

root = tkinter.Tk()
my_gui = Assignc3d(root, target_c3d, fields_c3d)
my_gui.fields_list.focus_set()
root.mainloop()
print(my_gui.assign)
