import tables
import os


def create_file(project_path):
    """Create HDF5 file and append some group."""
    filename = os.path.join(project_path, '', 'data.hdf5')
    file = tables.open_file(filename=filename, mode='w')
    file.create_group(where='/', name='metadata', title='Metadata')
    file.close()


def append_metadata(project_path, metadata, case):
    """Append metadata from csv files into HDF5 file"""
    filename = os.path.join(project_path, '', 'data.hdf5')
    file = tables.open_file(filename=filename, mode='a')

    descriptor = column_descriptor(case)
    table = file.create_table(file.root.metadata, name=case, description=descriptor, title=case + 'metadata')

    row = table.row
    for i in range(metadata.shape[0]):
        for name, values in metadata.iteritems():
            row[name] = values[i]
        row.append()
    table.flush()
    file.close()


def column_descriptor(case):
    """Skeleton for the column descriptor of the metadata tables"""
    class Descriptor(tables.IsDescription):
        if case is 'emg':
            muscle_id = tables.StringCol(16)
            publication_name = tables.StringCol(16)
        elif case is 'markers':
            marker_id = tables.StringCol(20)
        elif case is 'force':
            analog_id = tables.StringCol(16)
        elif case is 'participants':
            pseudo = tables.StringCol(16)
            process = tables.BoolCol()
            laterality = tables.StringCol(1)
            group = tables.Int32Col()
            mass = tables.Int32Col()
            height = tables.Int32Col()
            date = tables.StringCol(10)
        elif case is 'trials':
            folder = tables.StringCol(10)
            emg = tables.BoolCol()
            markers = tables.BoolCol()
            force = tables.BoolCol()
        else:
            raise ValueError('choose a valid descriptor case')

    return Descriptor
