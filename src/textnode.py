from enum import Enum
from types import NoneType


class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(
        self, text: str, text_type: TextType, url: str | NoneType = None
    ) -> None:
        self.text: str = text
        self.text_type: TextType = text_type
        self.url: str | NoneType = url

    def __eq__(self, other: "TextNode") -> bool:
        if self.text != other.text:
            return False
        if self.text_type != other.text_type:
            return False
        if self.url != other.url:
            return False
        return True

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
