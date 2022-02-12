"""Twitter Bot Client Implementation"""

from typing import Optional

from tbc.tbclib.config_parser import CfgParser


class TweepyWrapper:
    """tweepy wrapper for tbc"""

    def __init__(self, cfg: Optional[CfgParser]=None) -> None:
        

