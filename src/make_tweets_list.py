"""dev tools
"""
from pathlib import Path

import pandas as pd

img_path_list = list(Path('./img').glob('*.jpg'))
num_of_imgs = len(img_path_list)

tweets_raw = pd.read_csv('tweets-raw.csv')
tweets_exported = tweets_raw.copy()
tweets_exported['tweeted'] = 0

img_name_list = [''] * tweets_exported.shape[0]
for idx in range(len(img_name_list)):
    img_idx = idx % num_of_imgs
    img_name_list[idx] = img_path_list[img_idx].name

tweets_exported['imgName'] = img_name_list
tweets_exported.to_csv('tweets-tbl.csv')
