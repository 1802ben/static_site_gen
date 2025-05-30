from textnode import TextType, TextNode
import os
import shutil


print("hello world")


def main():
    TestNode = TextNode("This is some anchor text",
                         TextType.LINK, "https://www.site.dev")
    print(repr(TestNode))
    sync_directories("static", "public")

def sync_directories(src: str, dst: str):
    if os.path.exists(dst):
        shutil.rmtree(dst)

    os.makedirs(dst, exist_ok=True)

    def recursive_copy(current_src, current_dst):
        for item in os.listdir(current_src):
            s_path = os.path.join(current_src, item)
            d_path = os.path.join(current_dst, item)
            if os.path.isdir(s_path):
                os.makedirs(d_path, exist_ok=True)
                recursive_copy(s_path, d_path)
            else:
                shutil.copy2(s_path, d_path)

    recursive_copy(src, dst)




main()