# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field(default="No url")
    movie_name = scrapy.Field(default="No name")
    movie_premiere_location = scrapy.Field(default="No premiere location")
    movie_time = scrapy.Field(default="No time")
    movie_release_time = scrapy.Field(default="No release time")
    movie_class = scrapy.Field(default="No class")
    movie_introduction = scrapy.Field(default="No introduction")
