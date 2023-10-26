
scrapy shell -s USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36" https://ssr1.scrape.center/detail/9


**recorrect**
details = response.xpath('//div[@class="m-v-sm info"]//span/text()').extract()

2023-10-25 00:05:43 [scrapy.spidermiddlewares.httperror] INFO: Ignoring response <500 https://ssr1.scrape.center/page/11>: HTTP status code is not handled or not allowed

page11页打不开，所以一共100条数据，都已经爬取完毕


```python
# name
response.xpath("//h2[@class='m-b-sm']//text()").extract()

# premiere location
response.xpath('//div[@class="m-v-sm info"]//span/text()').extract()[0]

# time
response.xpath('//div[@class="m-v-sm info"]//span/text()').extract()[2]

# 这个有问题
response.xpath('//div[@class="m-v-sm info"]//span/text()').extract()[3]

# class
response.xpath('//div[@class="categories"]//button//text()').extract()


response.xpath('//div[@class="drama"]//p/text()').extract()


```

