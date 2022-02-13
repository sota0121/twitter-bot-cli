"""cmd args parse tests"""

import numpy as np
import pandas as pd
import pytest

from tbc import (
    validate_options_bot_send,
    validate_tweet_tbl_cols,
)

# ==============================
# command options validation
# ==============================
def test_bot_send_valid_msg_only():
    # Arange
    msg = "msg"
    img_file = None
    sel_rand = False
    sel_seq = None
    src = None

    # Act
    expected = True
    actual = validate_options_bot_send(msg, img_file, sel_rand, sel_seq, src)

    # Assert
    assert expected is actual

def test_bot_send_valid_msg_imgpath():
    # Arange
    msg = "msg"
    img_file = "img/path"
    sel_rand = False
    sel_seq = None
    src = None

    # Act
    expected = True
    actual = validate_options_bot_send(msg, img_file, sel_rand, sel_seq, src)

    # Assert
    assert expected is actual

def test_bot_send_valid_selrand():
    # Arange
    msg = None
    img_file = None
    sel_rand = True
    sel_seq = None
    src = None

    # Act
    expected = True
    actual = validate_options_bot_send(msg, img_file, sel_rand, sel_seq, src)

    # Assert
    assert expected is actual

def test_bot_send_valid_selrand_src():
    # Arange
    msg = None
    img_file = None
    sel_rand = True
    sel_seq = None
    src = "src/path"

    # Act
    expected = True
    actual = validate_options_bot_send(msg, img_file, sel_rand, sel_seq, src)

    # Assert
    assert expected is actual

def test_bot_send_valid_selseq():
    # Arange
    msg = None
    img_file = None
    sel_rand = False
    sel_seq = 1
    src = None

    # Act
    expected = True
    actual = validate_options_bot_send(msg, img_file, sel_rand, sel_seq, src)

    # Assert
    assert expected is actual

def test_bot_send_valid_selseq_src():
    # Arange
    msg = None
    img_file = None
    sel_rand = False
    sel_seq = 1
    src = "src/path"

    # Act
    expected = True
    actual = validate_options_bot_send(msg, img_file, sel_rand, sel_seq, src)

    # Assert
    assert expected is actual

def test_bot_send_invalid_msg_selrand():
    # Arange
    msg = "msg"
    img_file = None
    sel_rand = True
    sel_seq = None
    src = None

    # Act
    expected = False
    actual = validate_options_bot_send(msg, img_file, sel_rand, sel_seq, src)

    # Assert
    assert expected is actual

def test_bot_send_invalid_msg_selseq():
    # Arange
    msg = "msg"
    img_file = None
    sel_rand = False
    sel_seq = 1
    src = None

    # Act
    expected = False
    actual = validate_options_bot_send(msg, img_file, sel_rand, sel_seq, src)

    # Assert
    assert expected is actual

def test_bot_send_invalid_selrand_selseq():
    # Arange
    msg = None
    img_file = None
    sel_rand = True
    sel_seq = 1
    src = None

    # Act
    expected = False
    actual = validate_options_bot_send(msg, img_file, sel_rand, sel_seq, src)

    # Assert
    assert expected is actual

def test_bot_send_invalid_imgpath_only():
    # Arange
    msg = None
    img_file = "img/path"
    sel_rand = False
    sel_seq = None
    src = None

    # Act
    expected = False
    actual = validate_options_bot_send(msg, img_file, sel_rand, sel_seq, src)

    # Assert
    assert expected is actual

def test_bot_send_invalid_src_only():
    # Arange
    msg = None
    img_file = None
    sel_rand = False
    sel_seq = None
    src = "src/path"

    # Act
    expected = False
    actual = validate_options_bot_send(msg, img_file, sel_rand, sel_seq, src)

    # Assert
    assert expected is actual

def test_bot_send_invalid_no_msglike():
    # Arange
    msg = None
    img_file = None
    sel_rand = False
    sel_seq = None
    src = None

    # Act
    expected = False
    actual = validate_options_bot_send(msg, img_file, sel_rand, sel_seq, src)

    # Assert
    assert expected is actual

# ==============================
# source table validation
# ==============================
def test_src_tbl_valid_cols():
    # Arange
    _df = pd.DataFrame(data=np.arange(12).reshape(6, 2),
                       columns=["text", "imgName"])

    # Act
    expected = True
    actual = validate_tweet_tbl_cols(_df)

    # Assert
    assert expected is actual

def test_src_tbl_invalid_no_text_col():
    # Arange
    _df = pd.DataFrame(data=np.arange(12).reshape(3, 4),
                       columns=["a", "b", "c", "imgName"])

    # Act
    expected = False
    actual = validate_tweet_tbl_cols(_df)

    # Assert
    assert expected is actual

def test_src_tbl_invalid_no_imgname_col():
    # Arange
    _df = pd.DataFrame(data=np.arange(12).reshape(3, 4),
                       columns=["a", "b", "c", "text"])

    # Act
    expected = False
    actual = validate_tweet_tbl_cols(_df)

    # Assert
    assert expected is actual
