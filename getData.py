import requests
import re

csv_urls = []


def init():
    global csv_urls
    url = 'https://github.com/canghailan/Wuhan-2019-nCoV/tree/master/Data'
    res = requests.get(url)
    # 观察所得html文件后，使用正则表达式获取所需数据
    csv_urls = re.findall(r'href="/canghailan/Wuhan-2019-nCoV/blob/master/Data/(.*?).csv">', res.text)


def get_data():
    global csv_urls
    try:
        with open('cache.txt') as f:
            text = f.readlines()
            idx = csv_urls.index(text[0])
            csv_urls = csv_urls[idx+1:]
    except:
        pass# 此时cache.txt中数据被非法修改，选择不去除任何url，全部重新读取
    finally:
        for i in csv_urls:
            #获取url
            url = 'https://raw.githubusercontent.com/canghailan/Wuhan-2019-nCoV/master/Data/%s.csv' % i
            print(url) # 显示下载进度
            res = requests.get(url)
            #将获取的数据写入文件
            with open(f'data/{i}.csv', mode='w', encoding='utf-8') as f:
                f.writelines(res.text)
        if len(csv_urls)!= 0:
            with open('cache.txt',mode='w',encoding='utf-8') as f:
                f.write(csv_urls[-1])
