import random
from datetime import date
from typing import Optional

from tbc.tbclib.constants import *
from tbc.tbclib.errors import *
from tbc.tbclib.wrapper import TweepyWrapper as tw
from tbc.tbclib.wrapper import GspreadWrapper as gw
from tbc.tbclib.wrapper import GCSWrapper as gcsw


def get_date_idx() -> int:
    """Get index by date
    """
    today_date = date.today().day
    _target_idx = today_date - 1
    return _target_idx

def send_tweet(request):
    """Responds to any HTTP request.
    ## Args
    - request (flask.Request): HTTP request object.

    ## Note
    - This functions can be deployed to Google Cloud Functions

    ## Returns
    The response text or any set of values that can be turned into a
    Response object using
    `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    gcs_app = gcsw()
    tweets_df = gcs_app.tweets_df

    tweet_str = ""
    try:
        # get msg to send
        df_target_row = tweets_df.iloc[get_date_idx()]
        tweet_str = df_target_row[COL_TEXT]
        img_name = str(df_target_row[COL_IMGNAME])
        img_file = gcs_app.download_image_by_name(img_name)

        # send words
        tw_app = tw()
        media = tw_app.api.media_upload(filename="img.jpg", file=img_file)
        result = tw_app.api.update_status(status=tweet_str, media_ids=[media.media_id])
    except KeyError as e:
        tweet_str = "(Failed to tweet)"
        print(repr(e))
    except Exception as e:
        tweet_str = "(Failed to tweet)"
        print(repr(e))
    finally:
        return f'tweeted > \n{tweet_str}'


def send_tweet_from_cli(msg: str,
                        img_file: Optional[str] = None) -> None:
    tw_app = tw()
    if img_file is None:
        tw_app.api.update_status(status=msg)
    else:
        try:
            with open(img_file, 'rb') as f:
                media = tw_app.api.media_upload(filename='img.jpg', file=f)
                result = tw_app.api.update_status(status=msg,
                                                media_ids=[media.media_id])
        except Exception as e:
            print(repr(e))
            raise TbcError("Something has been wrong when sending tweet.")
