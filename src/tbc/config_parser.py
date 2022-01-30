"""config file parser
"""
import os
from pathlib import Path
from typing import Optional

from yaml import safe_load

from tbc.constants import *


class CfgParser:
    """config parser"""
    def __init__(self, path: Optional[str]=None) -> None:
        self._cfg_path = path
        self._load_envval()

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

