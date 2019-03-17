from decorators import skip
import yaml
import deepdish as dd
from pathlib import Path
import seaborn as sb
from visualization.visualise import plot_model_accuracy, plot_robot_position
from models.predict_model import predict
from data.create_eeg_dataset import eeg_dataset
from data.create_robot_dataset import robot_dataset
from data.clean_eeg_dataset import clean_dataset
from data.create_torch_dataset import torch_dataset
from data.create_torch_dataset import balanced_torch_dataset
from models.train_model import train
from decorators import skip_run_code

def get_model_path():
    path = str(Path(__file__).parents[1] / 'models')
    with open(path + '/time.txt', "r+") as f:
        time_stamp = f.readlines()
    time_stamp = time_stamp[-1][0:-1]
    model_path = path + '/model_' + time_stamp + '.pth'
    model_info_path = path + '/model_info_' + time_stamp + '.pth'

    return model_path, model_info_path


def save_dataset(path, dataset, save=False):
    if save:
        dd.io.save(save_path, clean_dataset)


with skip_run_code('skip', 'create_eeg_dataset') as check, check():
    eeg_dataset = create_dataset(config['subjects'], config['trials'])
    save_path = Path(__file__).parents[2] / config['raw_eeg_dataset']
    save_dataset(save_path, eeg_dataset)


with skip_run_code('skip', 'create_robot_dataset') as check, check():
    robot_dataset = create_dataset(config['subjects'], config['trials'])
    save_path = Path(__file__).parents[2] / config['raw_robot_dataset']
    save_dataset(save_path, robot_dataset)


with skip_run_code('skip', 'clean_eeg_dataset') as check, check():
    clean_dataset = clean_dataset(configp['subjects'], config['trials'])
    save_path = Path(__file__).parents[2] / config['clean_eeg_dataset']
    save_dataset(save_path, clean_dataset)


with skip_run_code('skip', 'torch_dataset') as check, check():
    torch_dataset = create_torch_dataset(subjects, trials, config)
    save_path = str(Path(__file__).parents[2] / config['torch_dataset'])
    save_dataset(save_path, torch_dataset)


with skip_run_code('skip', 'balanced_torch_dataset') as check, check():
    data_path = str(Path(__file__).parents[2] / config['torch_dataset'])
    balanced_dataset = create_balanced_dataset(data_path)
    save_path = str(Path(__file__).parents[2] / config['balanced_torch_dataset'])
    save_dataset(save_path, balanced_torch_dataset)
