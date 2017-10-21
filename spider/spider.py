# -*- coding:utf-8 -*-

import urllib
import re
import json
import requests
import os
import pymongo
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from hashlib import md5
from multiprocessing import Pool
import sys

from config import *


# client = pymongo.MongoClient(MONGO_URL,8000)
# db = client[MONGO_DB]
reload(sys)
sys.setdefaultencoding('utf8')

def get_page_index(offset, keyword):
    data = {'offset': offset,
            'format': 'json',
            'keyword': keyword,
            'autoload': 'true',
            'count': 20,
            'cur_tab': 3
            }
    url = 'http://www.toutiao.com/search_content/?' + urllib.urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print  ('请求索引失败 ')
        return None


def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')


def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print  ('请求详情页失败')
        return None


def parse_page_detail(html, url):
    soup = BeautifulSoup(html, "lxml")
    # print  '调用成功'
    title = soup.select('title')[0].get_text()
    images_pattern = re.compile('gallery: (.*?)siblingList:', re.S)
    result = re.search(images_pattern, html)
    if result:
        jsonString = result.group(1)
        # 这句话是解析的关键问题
        strJson = "".join([jsonString.strip().rsplit("}", 1)[0], "}"])
        data = json.loads(strJson)
        if data and "sub_images" in data.keys():
            sub_images = data.get("sub_images")
            images = [item.get("url") for item in sub_images]
            for image in images: download_image(image)
            return {
                'title': title,
                'url': url,
                'images': images
            }
        return None
    return None


# def save_to_mongo(result):
#     if db[MONGO_TABLE].insert(result):
#         # print ('存储到MongoDB成功')
#         return True

def download_image(url):
    print '正在下载图片 %s' % url
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_image(response.content)
        return None
    except RequestException:
        print  ('下载图片出错 ')
        return None


def save_image(content):

    imagePath = os.path.join(os.getcwd(),KEYWORD)
    if not os.path.exists(imagePath):
        os.mkdir(KEYWORD)

    file_path = '{0}/{1}.{2}'.format(imagePath, md5(content).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()


def start_spider(offset):
    html = get_page_index(offset, KEYWORD)
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            result = parse_page_detail(html, url)
            # save_to_mongo(result)


def main():
    # start_spider(20)
    print '开始爬虫 %s' % KEYWORD
    groups = [x * 20 for x in range(GROUP_START + 1, GROUP_END + 1)]
    print groups
    pool = Pool()
    pool.map(start_spider, groups)


if __name__ == '__main__':
    main()
