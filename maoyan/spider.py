# -*- coding:utf-8 -*-

import requests
from requests.exceptions import RequestException
import re
import json
from multiprocessing import Pool
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def get_one_page(url):
    try:
        headers = {'Cookie': 'uuid=1A6E888B4A4B29B16FBA1299108DBE9CA19BF5FFE6115FF5DB33C57435722EFC; __mta=252493494.1508603211173.1508603308257.1508603314017.11; _lxsdk_s=727305baebd98f615050b97d4a5a%7C%7C26',
                   'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求异常')
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d*)</i>.*? data-src="(.*?)".*?name"><a.*?'
                         +'>(.*?)</a>.*?star">(.*?)</p>.*?"releasetime">(.*?)</p>.*?'
                         +'"integer">(.*?)</i>.*?"fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2].decode('utf-8'),
            'actor':item[3],
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
        }

def save_to_file(content):
    with open('result.txt','a') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()


def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    for item in  parse_one_page(html):
        save_to_file(item)

if __name__ == '__main__':

    pool = Pool()
    pool.map(main,[i * 10 for i in range(10)])

