import imp
from enum import IntEnum
from enum import unique
from typing import Final


@unique
class TweetType(IntEnum):
    DATE_AS_KEY = 1 # use date as key of tweets list
    RAND_KEY = 2 # select randomized from tweets list

COL_TEXT: Final[str] = "text"
COL_TWT_FLG: Final[str] = "tweeted"
COL_IMGNAME: Final[str] = "imgName"

DEFAULT_RES_PATH: Final[str] = "./data"
DEFAULT_IMG_PATH: Final[str] = f"{DEFAULT_RES_PATH}/img"
DEFAULT_TXT_LIST_PATH: Final[str] = f"{DEFAULT_RES_PATH}/tweets-raw.csv"
DEFAULT_TWEET_TBL_DST: Final[str] = f"{DEFAULT_RES_PATH}/tweets-tbl.csv"


class TbcError(Exception):
    pass
