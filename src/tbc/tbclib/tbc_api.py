"""Entry points for TBC.

The main APIs that TBC exposes to manage twitter bot account.

    XX(): xxx
    YY(): yyy

"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class TweetContent:
    text: Optional[str] = None
    img_path: Optional[str] = None

    def text_is_empty(self) -> bool:
        return (self.text == "" or self.text is None)
