
import os
import sp_eng_data as ed

def test_path():
    setup_path = os.path.join(ed.csv_path(),'setup.py')
    print(setup_path)
    assert os.path.isfile(setup_path)

def test_data_exists():
    test_data_path = os.path.join(ed.csv_path(), '2017-08-21', 'pc01a_ahrsdata_20170821.csv')
    assert os.path.isfile(test_data_path)
