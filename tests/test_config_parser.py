import os
import tempfile

import pytest
import yaml

from tbc.config_parser import CfgParser



# file fixture
# https://docs.pytest.org/en/6.2.x/tmpdir.html
# https://docs.pytest.org/en/6.2.x/tmpdir.html#the-tmpdir-factory-fixture
# https://rinatz.github.io/python-book/ch08-02-pytest/
# -------------------------------
# Arrange-Act-Assert Style
# http://wiki.c2.com/?ArrangeActAssert


cfg_obj = {"ENV_1": '123', "ENV_2": "abc"}

# Arange
@pytest.fixture
def config_file(tmpdir):
    """config file"""
    tmpfile = tmpdir.join("config.yml")
    with tmpfile.open('w') as f:
        cfg_str = yaml.dump(cfg_obj)
        f.write(cfg_str)
    yield str(tmpfile)
    tmpfile.remove()


def test_load_envval(config_file):
    # Act - set value to envval
    CfgParser(config_file)

    # Assert
    assert os.getenv('ENV_1') == '123'
    assert os.getenv('ENV_2') == 'abc'
