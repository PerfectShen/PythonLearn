# python 抓取今日头条图集

## 获取spider运行权限
工程下载下来之后获取到spider文件夹的权限,
username为当前电脑登录用户名
```
cd /Users/{username}/PythonLearn/spider
```


## 运行脚本
开始抓包
```
python spider.py
```


## 异常情况

#### 如果未安装 pymongo

```
sudo pip install pymongo
```

#### 如果未安装 BeautifulSoup

```
sudo pip install BeautifulSoup4
```

## 待完善

#### 数据库存储抓取到的数据
由于网络原因,mac上mongodb数据库未安装成功,导致还无法将抓取到的数据存储到mongodb数据库中.


## 总结
使用python进行抓包大概分为:<br />
1.分析要抓取的网页的请求方式,数据处理方式.<br />
2.使用python对获取到的数据进行过滤(正则表达式)<br />
3.将抓取到的数据存储到数据库<br />
4.使用多线程加快任务执行速度<br />

## 结束语

>我们可以断言,没有激情,任何伟大的事业都不能完成. --黑格尔
