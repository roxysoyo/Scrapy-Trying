### Scrapy Notions
About Doc, details in [Python Scrapy](https://thepythonscrapyplaybook.com/freecodecamp-beginner-course/).
About Video, details in [Scrapy Course – Python Web Scraping for Beginners](https://youtu.be/mBoX_JCKZTE).
#### Specific steps
##### Step0: Creating Scrapy Project
```
# create a scrapy project
scrapy startproject <project_name>

# create a new generic spider
scrapy genspider bookspider books.toscrape.com
```
About **scrapy shell**:
```
# open Scrapy shell
scrapy shell

# make sure IPython installed
pip3 install ipython

# edit scrapy.cfg file like so:
## scrapy.cfg
[settings]
default = chocolatescraper.settings
shell = ipython
```

##### Step1: 获得需要爬取的item
可以使用css选择器，也可以是xpath语言。
建议xpath来定位item，css大多情况下适用性很差:disappointed_relieved:(Personal feelings)
Here are the examples:
```
response.css(".classname ::text").get() # ::text是伪类，获取文本信息
response.xpath('//div[@class="m-v-sm info"]//span/text()').extract()
```
如何查看是否定位到了目标item，可以使用scrapy shell终端来查看，在Vscode cmd窗口中输入"scrapy shell"。

当scrapy shell被阻止的时候，更换User-Agent:
scrapy shell -s USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36" https://movie.douban.com/top250

==Problems:==
1. 豆瓣电影TOP250网站，是提取不到信息的。但是如果点开具体的电影页面，就可以提取到了。
2. b站的up主页动态，则完全提取不到信息。

希望能够得到解答，thanks.
##### Step2: 确定网页之间的跳转
**"next page"** is crucial.

程序初步编写完成时，可以在终端输入一下代买，来查看是否爬取成功
```
scrapy crawl spidername
scrapy crawl spidername -O data.json # overwrite
scrapy crawl spidername -o data.json
```

##### Step3: 修改items.py文件
```
name = scrapy.Field()
name = scrapy.Field(default="No name")
```

##### Step4: 修改pipelines.py文件
For cleaning scrapy-data.

##### Step5: 修改middlewares.py文件
For modifying "User-Agent" and "Headers".
==Tips:==
1. 使用ScrapeOpsFakeUserAgentMiddleware的时候，必须开全局代理，否则[假代理网站](https://scrapeops.io/app/headers)登不上去。
2. 以上在各个.py文件中的修改，都要在settings.py文件中打开相关设置。

#### Project Description
目前，共有两个scrapy框架项目
1. [bookscraper](https://books.toscrape.com)
2. [caseqspider](https://ssr1.scrape.center)

#### Write behind
With new understanding, I will add this document note:sleepy:.