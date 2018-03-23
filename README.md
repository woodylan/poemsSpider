# poemsSpider
## 简介

这是用 [scrapy](https://github.com/scrapy/scrapy)  写的 [gushiwen.org](gushiwen.org) (古诗词)  爬虫工具。



## 环境

- python 3
- git

## 依赖

```shell
pip3 install beautifulsoup4
```


## 使用

1、下载本工具

```shell
git clone git@github.com:woodylan/poemsSpider.git
```


2、开始导出

~~~shell
scrapy crawl poems -o items.json
~~~



