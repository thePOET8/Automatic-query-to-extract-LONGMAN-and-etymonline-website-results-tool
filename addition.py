#因为我想保留原本的颜色样式，所以还是用了打开原网页，后续可能有改进
import webbrowser
import time
from tkinter import Tk, simpledialog

def search_word(word):
    urls = [
        f"https://www.ldoceonline.com/dictionary/{word}",
        f"https://www.etymonline.com/word/{word}#etymonline_v_14014"
    ]

    for url in urls:
        webbrowser.open(url)
        time.sleep(1)

def get_word_from_user():
    root = Tk()
    root.withdraw()  # 不显示主窗口
    word = simpledialog.askstring("输入", "请输入想搜索的单词:")
    if word:
        search_word(word)
    root.destroy()

get_word_from_user()