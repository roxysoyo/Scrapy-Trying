import scrapy
from case1spider.items import MovieItem


class MoviespiderSpider(scrapy.Spider):
    name = "moviespider"
    allowed_domains = ["ssr1.scrape.center"]
    start_urls = ["https://ssr1.scrape.center/"]

    def parse(self, response):
        movies = response.css(".el-card__body")
        for movie in movies:
            relative_url = movie.css("a").attrib["href"]
            movie_url = "https://ssr1.scrape.center" + relative_url
            yield response.follow(movie_url, callback=self.parse_movie_page)

        ## Next Page
        next_page = response.css(".next ::attr(href)").get()
        if next_page is not None:
            next_page_url = "https://ssr1.scrape.center" + next_page
            yield response.follow(next_page_url, callback=self.parse)

    def parse_movie_page(self, response):
        movie = response.xpath('//div[@class="item el-row"]')

        movie_item = MovieItem()
        movie_item["url"] = response.url
        movie_item["movie_name"] = movie.css(".m-b-sm ::text").get()

        details = movie.xpath('//div[@class="m-v-sm info"]//span/text()').extract()
        num_details = len(details)

        movie_item["movie_premiere_location"] = details[0]
        movie_item["movie_time"] = details[2]

        if num_details == 4:
            movie_item["movie_release_time"] = details[3]
        else:
            movie_item["movie_release_time"] = details[1]
            
        movie_item["movie_class"] = movie.xpath(
            '//div[@class="categories"]//button//text()'
        ).extract()
        movie_item["movie_introduction"] = movie.xpath(
            '//div[@class="drama"]//p/text()'
        ).extract()
        yield movie_item
