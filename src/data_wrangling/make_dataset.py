import os
import shutil
from pyprojroot import here
from dotenv import load_dotenv, find_dotenv
from kaggle.api.kaggle_api_extended import KaggleApi

def download_competition_data(comp_name='playground-series-s3e12'):
    '''
    Downloads and extracts the data from the specified Kaggle competition name into data/raw
    '''
    #cool little function that finds the root dir by looking for files commonly found there (like .git)
    proj_dir = here()
    # find .env automagically by walking up directories until it's found
    dotenv_path = find_dotenv()
    #load contents of the .env file as environment variables
    load_dotenv(dotenv_path)
    data_dir = os.path.join(proj_dir, 'data')
    raw_data_dir = os.path.join(data_dir, 'raw')
    if not os.path.exists(raw_data_dir):
        os.makedirs(raw_data_dir)

    api = KaggleApi()
    api.authenticate()
    api.competition_download_files(comp_name, path=raw_data_dir)
    shutil.unpack_archive(raw_data_dir + '\\' + comp_name + '.zip' , raw_data_dir)
    os.remove(raw_data_dir + '\\' + comp_name + '.zip')