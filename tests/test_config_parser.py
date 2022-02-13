import os
import shutil
import tempfile
import unittest

import pytest
import yaml

from tbc.tbclib.config_parser import *


# file fixture
# https://docs.pytest.org/en/6.2.x/tmpdir.html
# https://docs.pytest.org/en/6.2.x/tmpdir.html#the-tmpdir-factory-fixture
# https://rinatz.github.io/python-book/ch08-02-pytest/
# https://www.m3tech.blog/entry/pytest-summary
# -------------------------------
# Arrange-Act-Assert Style
# http://wiki.c2.com/?ArrangeActAssert


cfg_name = ".tbcconfig.yml"

# =============================
# CfgParser
# ----------
# See: yapf/yapftests/file_resources_test.py
# https://github.com/google/yapf/blob/main/yapftests/file_resources_test.py
# =============================

_correct_cfg_obj = {
    "version": "1",
    "twitter": {
        "consumer_key": "CONSUMER_KEY",
        "consumer_secret": "CONSUMER_SECRET",
        "access_token": "ACCESS_TOKEN",
        "access_secret": "ACCESS_SECRET"
    },
    "source": {
        "type": "local",
        "local_path": "src/data/tweets-tbl.csv",
        "gcs_path": "path/to/cloud/storage/table.csv",
        "gspread_path": "path/to/spreadsheet/table",
    }
}

_no_twtoken_cfg_obj = {
    "version": "1",
    "twitter": {
        "consumer_key": "",
        "consumer_secret": "",
        "access_token": "",
        "access_secret": ""
    },
    "source": {
        "type": "local",
        "local_path": "src/data/tweets-tbl.csv",
        "gcs_path": "path/to/cloud/storage/table.csv",
        "gspread_path": "path/to/spreadsheet/table",
    }
}

@pytest.fixture
def cfg_file_no_twtoken(tmpdir):
    cfg_tmpfile = tmpdir.join(cfg_name)
    with cfg_tmpfile.open('w') as f:
        cfg_str = yaml.dump(_no_twtoken_cfg_obj)
        f.write(cfg_str)
    yield str(cfg_tmpfile)
    cfg_tmpfile.remove()

@pytest.fixture
def cfg_file_correct(tmpdir):
    cfg_tmpfile = tmpdir.join(cfg_name)
    with cfg_tmpfile.open('w') as f:
        cfg_str = yaml.dump(_correct_cfg_obj)
        f.write(cfg_str)
    yield str(cfg_tmpfile)
    cfg_tmpfile.remove()


def test_correct_cfg(cfg_file_correct):
    # Act
    cfg: TbcConfig = CfgParser.load(cfg_file_correct)

    # Assert
    assert cfg.ver == _correct_cfg_obj["version"]
    assert cfg.tw_consumer_key == _correct_cfg_obj["twitter"]["consumer_key"]
    assert cfg.tw_consumer_secret == _correct_cfg_obj["twitter"]["consumer_secret"]
    assert cfg.tw_access_token == _correct_cfg_obj["twitter"]["access_token"]
    assert cfg.tw_access_secret == _correct_cfg_obj["twitter"]["access_secret"]
    assert cfg.src_type == 0 # SrcType.local.value
    assert cfg.src_lo_path == _correct_cfg_obj["source"]["local_path"]
    assert cfg.src_gcs_path == _correct_cfg_obj["source"]["gcs_path"]
    assert cfg.src_gspr_path == _correct_cfg_obj["source"]["gspread_path"]
    assert cfg.twitter_tokens_exist() is True


def test_no_twtoken_cfg(cfg_file_no_twtoken):
    # Act
    cfg: TbcConfig = CfgParser.load(cfg_file_no_twtoken)

    # Assert
    assert cfg.twitter_tokens_exist() is False


# =============================
# TbcConfig
# =============================
def test_tbccfg_empty():
    # Arrange / Act
    cfg = TbcConfig()

    # Assert
    assert cfg.twitter_tokens_exist() is False

def test_tbccfg_partial_empty():
    # Arrange / Act
    cfg = TbcConfig()
    cfg.tw_consumer_key = "consumer_key"

    # Assert
    assert cfg.twitter_tokens_exist() is False

def test_tbccfg_fulfilled():
    # Arrange
    cfg = TbcConfig()

    # Act
    cfg.tw_consumer_key = "consumer_key"
    cfg.tw_consumer_secret = "consumer_secret"
    cfg.tw_access_token = "access_token"
    cfg.tw_access_secret = "access_secret"

    # Assert
    assert cfg.twitter_tokens_exist() is True

