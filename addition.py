#因为我想在复制时保留原网页的样式和颜色，所以目前还有直接打开的方式，后续会改进
import webbrowser
import time


def search_word(word):
    # 定义搜索的URL
    urls = [
        f"https://www.ldoceonline.com/dictionary/{word}",
        f"https://www.etymonline.com/word/{word}#etymonline_v_14014"
    ]

    for url in urls:
        # 使用默认浏览器打开URL
        webbrowser.open(url)

        # 在每个请求之间添加延时，以避免同时打开太多标签
        time.sleep(1)


# 测试函数
search_word("flaw")