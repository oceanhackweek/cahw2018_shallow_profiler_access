
import os
import pandas as pd


__CSV_PATH__ = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))


def csv_path():
    return __CSV_PATH__

def load_sp_eng_data(platform, source='csv' ):
    if source == 'csv':
        print('csv')
    else:
        print('M2M')
        ## Load through M2M
