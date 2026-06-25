from types import NoneType

from textnode import TextNode, TextType


def main() -> NoneType:
    print(TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev"))


if __name__ == "__main__":
    main()
