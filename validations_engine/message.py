"""Message class."""
from dataclasses import dataclass
from typing import Union


@dataclass
class Message:
    """
    Message dataclass.

    This class helps to ensure that the message are all
     in the same type to be sent to GChat.
    """

    content: str
    destination: Union[str, None]
