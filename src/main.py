from textnode import *

print("hello world")


def main():
    TestNode = TextNode("This is some anchor text",
                         TextType.LINK, "https://www.site.dev")
    print(repr(TestNode))

main()