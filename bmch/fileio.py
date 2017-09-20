# -*- coding: utf-8 -*-
# TODO: doc


def create_conf_file(path, files):
    import pandas as pd
    import json

    # read each csv files into dict
    d = {name: pd.read_csv('{}{}.csv'.format(path, name)) for name in files}

    # merge dicts into json files
    z = {k: json.loads(d[k].to_json()) for k in d}

    # export json file
    outpath = '{}config.json'.format(path)
    with open(outpath, 'w') as out:
        out.write(json.dumps(z, indent=4))
