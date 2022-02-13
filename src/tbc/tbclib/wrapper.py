"""Wrappe for not main proc (like autharization)
"""
from io import BytesIO
from os import getenv
import json

import gspread
from google.cloud import storage
import pandas as pd
import tweepy

from tbc.tbclib.config_parser import TbcConfig


class TweepyWrapper:

    def __init__(self, cfg: TbcConfig) -> None:
        consumer_key = cfg.tw_consumer_key
        consumer_secret = cfg.tw_consumer_secret
        access_token = cfg.tw_access_token
        access_secret = cfg.tw_access_secret

        self.__auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.__auth.set_access_token(access_token, access_secret)
        self.__api = tweepy.API(self.__auth)

    @property
    def api(self):
        return self.__api


TWEETS_LIST_SPREAD_SHEET_NAME = "twitter-bot-positive-demon"

class GspreadWrapper:

    def __init__(self) -> None:
        _credentials = {
            "TYPE": getenv("gs_type"),
            "PROJECT_ID": getenv("gs_project_id"),
            "PRIVATE_KEY_ID": getenv("gs_private_key_id"),
            "PRIVATE_KEY": getenv("gs_private_key"),
            "CLIENT_EMAIL": getenv("gs_client_email"),
            "CLIENT_ID": getenv("gs_client_id"),
            "AUTH_URI": getenv("gs_auth_uri"),
            "TOKEN_URI": getenv("gs_token_uri"),
            "AUTH_PROVIDER_X509_CERT_URL": getenv("gs_auth_provider_x509_cert_url"),
            "CLIENT_X509_CERT_URL": getenv("gs_client_x509_cert_url")
        }
        _service_account = gspread.service_account_from_dict(_credentials)
        self.__ws = _service_account.open(TWEETS_LIST_SPREAD_SHEET_NAME)
        self.__tweets = self.__ws.sheet1.get('A1')

    @property
    def worksheet(self):
        return self.__ws

    @property
    def tweets(self):
        return self.__tweets


BUCKET_NAME = "tweet-source"
#TWEETS_LIST_BLOB_NAME = "tweets_list.json"
TWEETS_LIST_BLOB_NAME = "tweets-tbl.csv"
IMG_LIST_FOLDER_NAME = "img"

class GCSWrapper:

    def __init__(self) -> None:
        _storage_client = storage.Client()
        self.__bucket = _storage_client.bucket(BUCKET_NAME)
        self.__blob = self.__bucket.blob(TWEETS_LIST_BLOB_NAME)
        _blob_bin = self.__blob.download_as_bytes()
        self.__tweets_df = pd.read_csv(BytesIO(_blob_bin))
        # _blob_txt = self.__blob.download_as_text()
        # self.__tweets_list = json.loads(_blob_txt)

    @property
    def tweets_df(self) -> pd.DataFrame:
        return self.__tweets_df

    def update_tweets(self, tweets: list):
        try:
            self.__blob.upload_from_string(data=json.dumps(tweets), content_type='application/json')
        except:
            print('failed to upload json (I will solve this problem in a few days.)')

    def download_image_by_name(self, img_name: str) -> BytesIO:
        _blob_img = self.__bucket.blob(f"{IMG_LIST_FOLDER_NAME}/{img_name}")
        _blob_bin = _blob_img.download_as_bytes()
        return BytesIO(_blob_bin)