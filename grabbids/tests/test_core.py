import pytest
from grabbids import Layout
from os.path import join, dirname
from pprint import pprint


def test_full():
    data_dir = join(dirname(__file__), 'data', '7t_trt')
    layout = Layout(data_dir)
    # result = layout.get(subject='[1234]', run='1', return_type='tuple')
    # result = layout.unique('subject')
    # result = layout.count('run')
    # result = layout.get(subject='sub-0[12]', run=1, extensions='.nii.gz')
    # result = layout.get(target='type', return_type='id', subject=1)
    # result = layout.as_data_frame(session=1)
    # pprint([f.filename for f in result[:5]])
    result = layout.find_match(target='bval', source='/Users/tal/Dropbox/Code/grabbids/grabbids/tests/data/7t_trt/sub-03/ses-2/func/sub-03_ses-2_task-rest_acq-fullbrain_run-2_bold.nii.gz')
    print(result)

test_full()