import deepdish as dd
from pathlib import Path
import deepdish
import pytest
import yaml
import h5py
import numpy as np

# Configuration files
path = Path(__file__).parents[1] / 'src/config.yml'
config = yaml.load(open(path))
epoch_length = config['epoch_length']
subjects = config['subjects']
trials = config['trials']


# @pytest.mark.skip(reason='slow')
def test_eeg_dataset_length():
    """Test the number of subjects in eeg dataset.

    Returns
    -------
    Assertion with respect to the total number of subjects
    """
    # Raw dataset
    path = str(Path(__file__).parents[1] / config['raw_eeg_dataset'])
    data = dd.io.load(path)
    assert (len(data.keys()) == len(subjects))

    # Clean dataset
    path = str(Path(__file__).parents[1] / config['clean_eeg_dataset'])
    data = dd.io.load(path)
    assert (len(data.keys()) == len(subjects))


@pytest.mark.skip(reason='need to do')
def test_robot_dataset_length():
    """Test the number of subjects in robot dataset.

    Returns
    -------
    Assertion with respect to the total number of subjects
    """
    # Raw data
    path = str(Path(__file__).parents[1] / 'data/interim/robot_dataset.h5')
    data = dd.io.load(path)
    assert (len(data.keys()) == len(subjects))


@pytest.mark.skip(reason='need to do')
def test_torch_dataset_length():
    """Test whether number of features and labels are same.

    Returns
    -------
    Assertion whether total features and labels are equal.
    """
    # Raw data
    path = str(Path(__file__).parents[1] / 'data/processed/torch_dataset.h5')
    data = dd.io.load(path)
    n_features = data['features'].shape[0]
    n_labels = data['labels'].shape[0]

    assert (n_labels == n_features)


@pytest.mark.skip(reason='need to do')
def test_data_iterator_ids():
    """Short summary.

    Returns
    -------
    Assertion whether length of test id is equal to length of validate id

    """
    from src.models.utils import data_iterator_ids
    path = str(Path(__file__).parents[1] / 'data/processed/torch_dataset.h5')
    ids_list = data_iterator_ids(path, test_size=0.15)

    # Check validation and testing data size
    assert abs(len(ids_list['validation']) - len(ids_list['testing'])) < 2


@pytest.mark.skip(reason='need to do')
def test_data_balance():
    """Test if data is balanced.
    Returns
    -------
        Assertion whether the chance is less than 35%

    """
    path = str(Path(__file__).parents[1]
               / 'data/processed/balanced_torch_dataset.h5')
    data = dd.io.load(path)
    labels = np.array(data['labels'])
    sum = np.sum(labels, axis=0) / len(labels)

    assert (sum < 0.36).all()
