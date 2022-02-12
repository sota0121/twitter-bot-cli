"""dev tools
"""
from pathlib import Path

import pandas as pd

from tbc.tbclib.constants import *


class TweetTableMaker:
    """tweets table maker"""

    def __init__(self, img_src_dir: str, txt_src_path: str, dst_path: str) -> None:
        self._img_src = img_src_dir
        self._txt_src_path = txt_src_path
        self._dst_path = dst_path

    def make(self):
        """Make tweets table from raw data

            ## Input Data
            - img files (in self._img_src)
            - txt_src csv file

            ## Output
            - tweet text table (path : self._dst_path)
        """
        # Get image file pathes
        _target_extensions = ['png', 'jpg', 'jpeg', 'gif']
        _img_path_list = []
        for ext in _target_extensions:
            _cur_path_list = list(Path(self._img_src).glob(f'*.{ext}'))
            _img_path_list.extend(_cur_path_list)

        # Get text table
        tweets_raw = pd.read_csv('tweets-raw.csv')
        tweets_exported = tweets_raw.copy()
        tweets_exported[COL_TWT_FLG] = 0

        # Make image name list
        num_of_imgs = len(_img_path_list)
        img_name_list = [''] * tweets_exported.shape[0]
        if num_of_imgs > 0:
            for idx in range(len(img_name_list)):
                img_idx = idx % num_of_imgs
                img_name_list[idx] = _img_path_list[img_idx].name

        tweets_exported[COL_IMGNAME] = img_name_list
        tweets_exported.to_csv(self._dst_path)
