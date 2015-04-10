# checks current APOTD website for title. return title and URL

import scrapy
from scrappyDemo.items import Website

class aptod(scrapy.Spider):
    name = "apotd"
    allowed_domains = ["apod.nasa.gov"]
    start_urls = [ "http://apod.nasa.gov/apod/astropix.html" ]

    def parse(self, response): #parses response data

        websiteItem = Website()
        selection = response.xpath('/html/body/center[2]/b[1]')

        websiteItem['name'] = "APOTD Title"
        websiteItem['description'] = selection.xpath('text()').extract()
        websiteItem['url'] = response
        yield websiteItem
