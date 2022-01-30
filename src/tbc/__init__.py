from typing import Optional

import click

from tbc.constants import *
from tbc.send_tweet import send_tweet, send_tweet_from_cli
from tbc.make_tweets_list import TweetTableMaker


@click.group()
def main() -> None:
    pass

@main.command()
@click.option(
    "-m",
    "--msg",
    type=str,
    help=(
        "[Option] Message to send"
        "e.g. tbc send -m \"Hello Twitter!\""
    )
)
@click.option(
    "-mf",
    "--msg-file",
    type=str,
    help=(
        "[Option] Text file path that msg is written"
        "e.g. tbc send -mf ./msg.txt"
    )
)
@click.option(
    "-i",
    "--img-file",
    type=str,
    help=(
        "[Option] Image file path to upload"
        "e.g. tbc send -i ./test.jpg"
    )
)
def send(msg: Optional[str]=None,
         msg_file: Optional[str]=None,
         img_file: Optional[str]=None) -> None:
    """send tweet command"""
    # Parse args
    if (msg is None) and (msg_file is None):
        print("No message is set.")
    elif (msg is not None) and (msg_file is not None):
        print("--msg and --msg-file option can be used only one of them.")
    else:
        _msg_text = ""
        if msg is not None:
            _msg_text = msg
        else:
            with open(msg_file, 'r') as f:
                _msg_text = f.read()
        try:
            if img_file is None:
                send_tweet_from_cli(_msg_text)
            else:
                send_tweet_from_cli(_msg_text, img_file)
            print("successfully tweeted")
        except Exception as e:
            print(f"something is wrong ... ({repr(e)})")


if __name__ == "__main__":
    main()
