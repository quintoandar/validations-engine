from dataclasses import dataclass
from typing import Union


@dataclass
class Message:
    content: str
    destination: Union[str, None]
