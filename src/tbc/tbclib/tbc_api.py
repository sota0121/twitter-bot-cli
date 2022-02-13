"""Entry points for TBC.

The main APIs that TBC exposes to manage twitter bot account.

    XX(): xxx
    YY(): yyy

"""

from dataclasses import dataclass


@dataclass
class TweetContent:
    text: str = ""
    img_path: str = ""

    def text_is_empty(self) -> bool:
        return (self.text == "" or self.text is None)
