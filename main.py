import requests
from bs4 import BeautifulSoup
import time


def search_word(word):
    # 定义搜索的URL
    urls = [
        f"https://www.ldoceonline.com/dictionary/{word}",
        f"https://www.etymonline.com/search?q={word}"
    ]

    # 定义请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    for url in urls:
        try:
            # 发送GET请求，包含请求头
            response = requests.get(url, headers=headers)
            # 解析HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # 根据网站结构提取信息，这里需要根据实际情况调整
            if "ldoceonline" in url:
                # 假设我们想提取词义部分
                results = soup.find_all('span', class_=['DEF', 'HYPHENATION','PronCodes','tooltip LEVEL','FREQ','GRAM','sensenum','PROPFORMPREP','neutral','REFHWD','EXAMPLE','HEADING','collo','asset','HWD','CENTURY','LANG','ORIGIN','TRAN'])
                print(f"Results from {url}:")
                for result in results:
                    print(result.text)
            elif "etymonline" in url:
                # 假设我们想提取词源信息
                result = soup.find('section', class_='word__defination--2q7ZH')
                print(f"Results from {url}:")
                print(result.text if result else "No etymology found.")
            print("\n")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")

        # 在每个请求之间添加延时
        time.sleep(1)


# 测试函数
search_word("example")