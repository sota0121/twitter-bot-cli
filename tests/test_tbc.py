import os
import tempfile

import pytest

from tbc.config_parser import CfgParser


class TestCfgParser:
    def setup(self):
        pass

    def test_load_envval(self):
        test_file_name = './tests/test.yml'
        cfg = "ENV_1: 123\nENV_2: abc"
        with open(test_file_name, 'w') as f:
            f.write(cfg)

        CfgParser(test_file_name)
        os.unlink(test_file_name)
        assert os.getenv('ENV_1') == '123'
        assert os.getenv('ENV_2') == 'abc'
