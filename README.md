项目实例：

一个学习scrapy的简单实例。帮助你快速的上手scrapy框架。

只需修改2个python文件。items.py 和spiders文件夹中的shushan.py。

需要修改的项，在2个python文件中均进行了备注。

大家可根据备注修改相关内容，再通过命令行运行爬虫程序。

命令行cd至spider目录,运行scrapy crawl shushan -o shushan.csv，生成csv文件，保存爬虫数据。

备注：保存的爬虫数据csv格式，需用WPS版excel打开，或是用txt直接打开。

代码下载：https://github.com/ABCnelson/scrapy-

图文说明网址：https://www.sohu.com/a/235695387_100064227

1.打开test100文件夹

里面包含了scrapy常用命令和说明

2.打开test100/test100文件夹

里面包含items.py等文件

3.简单实例只需要修改items.py文件和spiders文件夹中的shushan.py。打开items.py。

items类只包含需要下载的数据项的名称。根据自己要抓取的网页内容，添加项目名称，有多少要下载的column，添加多少项名称。

4.打开spiders文件夹

spiders文件夹里面有shushan.py

5.打开shushan.py文件

总计20多行代码

代码里面需要修改的内容，都有备注。中间需要学习xpath语法。地址：http://www.w3school.com.cn/xpath/xpath_syntax.asp

大家可根据备注修改相关内容，再通过命令行运行爬虫程序。

6.命令行cd至spider目录,运行scrapy crawl shushan -o shushan.csv，生成csv文件，保存爬虫数据。

备注：保存的爬虫数据csv格式，需用WPS版excel打开，或是用txt直接打开。

代码下载：https://github.com/ABCnelson/scrapy-
