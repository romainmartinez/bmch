# -*- coding: utf-8 -*-
import c3d
import tkinter

"""
- 1st dimension: X
- 2nd dimension: Y
- 3rd dimension: Z
- 4th dimension: error (useless)
- 5th dimension: cameras used (useless)
"""


def main(file_path, metadata=False, data=False):
    output_metadata, output_data = None, None
    with open(file_path, 'rb') as read:
        handler = c3d.Reader(read)
        if metadata:
            output_metadata = get_metadata(handler)
        if data:
            output_data = get_data()
    return output_metadata,  output_data


def get_metadata(handler):
    metadata = {
        'first_frame': handler.first_frame(),
        'last_frame': handler.last_frame(),

        'point_rate': handler.point_rate,
        'analog_rate': handler.analog_rate,

        'point_used': handler.point_used,
        'analog_used': handler.analog_used,

        'point_labels': handler.groups['POINT'].params['LABELS'].string_array,
        'analog_labels': handler.groups['ANALOG'].params['LABELS'].string_array
    }
    return metadata


def get_data():
    return 1


if __name__ == '__main__':
    filepath = '/home/romain/Downloads/irsst/inputs/IRSST_DapO/trials/DapOF6H1_1.c3d'
    #meta = main(filepath, metadata=True)
    assign_fields()
