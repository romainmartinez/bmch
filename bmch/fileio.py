import tables
import os


def create_file(project_path):
    filename = os.path.join(project_path, '', 'data.hdf5')
    file = tables.open_file(filename=filename, mode='w')
    file.close()


def append_metadata(project_path, metadata=None):
    filename = os.path.join(project_path, '', 'data.hdf5')
    # file = tables.open_file(filename=filename, mode='a')
    #
    # group = file.create_group(where='/', name='metadata', title='MetaData')
    #
    # filters = tables.Filters(complevel=5, complib='blosc')
    #
    # data = file.create_carray(file.root, metadata, 'metadata',
    #                           atom=tables.StringAtom,
    #                           shape=(0,),
    #                           filters=filters)
    # data[:] = metadata
    #
    # file.close()
    metadata.to_hdf(filename, 'table', mode='a')



if __name__ == '__main__':
    import pandas as pd
    path = '/home/romain/Downloads/irsst/'
    df = pd.read_csv(path + 'metadata/emg.csv')
    append_metadata(path, metadata=df)
