"""config file parser
"""
import os
import sys
from dataclasses import dataclass
from enum import (Enum, IntEnum, unique)
from pathlib import Path
from typing import (Final, Optional)

from yaml import safe_load
from tbc.tbclib.constants import *
from tbc.tbclib.errors import *


@unique
class SrcType(IntEnum):
    """Tweet Seed Table Type"""
    local = 0 # local file
    gcs = 1 # google cloud storage
    gspread = 2 # google spread sheet


# config keys
@unique
class CfgKeys(Enum):
    """Config File Keys

        ### Usage
        - get num of keys: len(CfgKeys)
        - get attr name: CfgKeys.ver_.name
        - get attr value: CfgKeys.ver_.value
    """
    # version
    ver_ = "version"
    # twitter
    tw_ = "twitter"
    tw_cns_key = "consumer_key"
    tw_cns_secret = "consumer_secret"
    tw_acc_token = "access_token"
    tw_acc_secret = "access_secret"
    # source
    src_ = "source"
    src_type = "type"
    src_lo_path = "local_path"
    src_gcs_path = "gcs_path"
    src_gspr_path = "gspread_path"


@unique
class EnvKeys(Enum):
    """Env Keys
        ### Usage
        - get num of keys: len(EnvKeys)
        - get attr name: EnvKeys.ver_.name
        - get attr value: EnvKeys.ver_.value
    """
    # twitter
    tw_cns_key = "TW_CONSUMER_KEY"
    tw_cns_secret = "TW_CONSUMER_SECRET"
    tw_acc_token = "TW_ACCESS_TOKEN"
    tw_acc_secret = "TW_ACCESS_SECRET"

    # source
    src_type = "SRC_TYPE"
    src_lo_path = "SRC_LOCAL_PATH"
    src_gcs_path = "SRC_GCS_PATH"
    src_gspr_path = "SRC_GSPREAD_PATH"


@dataclass
class TbcConfig:
    """tbc config obj"""
    # version
    ver: str = ""

    # twitter
    tw_consumer_key: str = ""
    tw_consumer_secret: str = ""
    tw_access_token: str = ""
    tw_access_secret: str = ""

    # src
    src_type: int = SrcType.local.value
    src_lo_path: str = ""
    src_gcs_path: str = ""
    src_gspr_path: str = ""
    # keys ... future impl

    def twitter_tokens_exist(self) -> bool:
        """Checks if twitter token info exists or not

            twitter api tokens must be set
        """
        if (self.tw_consumer_key == "") or (self.tw_consumer_secret == "") or (
                self.tw_access_token == "") or (self.tw_access_secret == ""):
            return False
        return True


class CfgParser:
    """config parser"""
    def __init__(self, path: Optional[str]=None) -> None:
        pass

    @staticmethod
    def load(path: Optional[str]=None) -> TbcConfig:
        """Load Config Values and Return Config Object

            if path set, load config values from the file
            else load config values from ENVIRONMENTS VALUE

        """
        cfg: TbcConfig = TbcConfig()
        # Load from tbc config file
        if path is not None:
            try:
                cfg_file = Path(path)
                if not cfg_file.exists():
                    raise FileNotFoundError(f"{MSG_ERR_LOAD_CFG} ({path})")
                with open(path, 'r') as f:
                    obj = safe_load(f)
                    # version
                    cfg.ver = obj.get(CfgKeys.ver_.value, "1")

                    # twitter
                    tw_obj = obj.get(CfgKeys.tw_.value, {})
                    cfg.tw_consumer_key = tw_obj.get(CfgKeys.tw_cns_key.value, "")
                    cfg.tw_consumer_secret = tw_obj.get(CfgKeys.tw_cns_secret.value, "")
                    cfg.tw_access_token = tw_obj.get(CfgKeys.tw_acc_token.value, "")
                    cfg.tw_access_secret = tw_obj.get(CfgKeys.tw_acc_secret.value, "")

                    # source
                    src_obj = obj.get(CfgKeys.src_.value, {})
                    cfg.src_type = SrcType[str(src_obj.get(CfgKeys.src_type.value, SrcType.local.name))].value
                    cfg.src_lo_path = src_obj.get(CfgKeys.src_lo_path.value, "")
                    cfg.src_gcs_path = src_obj.get(CfgKeys.src_gcs_path.value, "")
                    cfg.src_gspr_path = src_obj.get(CfgKeys.src_gspr_path.value, "")
            except Exception as e:
                raise TbcError(f"failed load tbcconfig ({path})")
        # Load from environments
        else:
            # twitter
            cfg.tw_consumer_key = os.getenv(EnvKeys.tw_cns_key.value, "")
            cfg.tw_consumer_secret = os.getenv(EnvKeys.tw_cns_secret.value, "")
            cfg.tw_access_token = os.getenv(EnvKeys.tw_acc_token.value, "")
            cfg.tw_access_secret = os.getenv(EnvKeys.tw_acc_secret.value, "")

            # source
            cfg.src_type = SrcType[os.getenv(EnvKeys.src_type.value, SrcType.local.name)].value
            cfg.src_lo_path = os.getenv(EnvKeys.src_lo_path.value, "")
            cfg.src_gcs_path = os.getenv(EnvKeys.src_gcs_path.value, "")
            cfg.src_gspr_path = os.getenv(EnvKeys.src_gspr_path.value, "")
        return cfg

    def _load_envval(self) -> None:
        try:
            cfg_file = Path(self._cfg_path)
            if cfg_file.exists():
                with open(self._cfg_path, 'r') as f:
                    obj = safe_load(f)
                    for k, v in obj.items():
                        os.environ[k] = v
        except Exception as e:
            raise TbcError(f"failed to load environ file ({self._cfg_path})")
