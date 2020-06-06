# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class SpokaneSpider(scrapy.Spider):
    name = 'Spokane'

#     def remove_characters(self, value):
#         return value.strip('\xa0')
    
    def start_requests(self):
        yield SeleniumRequest(
            url='https://www.spokanecounty.org/352/Inmate-Roster',
            wait_time=3,
            callback=self.parse
        )

    def parse(self, response):
        products = response.xpath("//*")
        for product in products:
            yield {
                'Date': product.xpath('//*[@id="aspnetForm"]/div[3]/h1').get(),
                'County': product.xpath("/html/head/title").get()\
#                 'State'
#                 'Pop_Count': self.remove_characters(product.xpath("normalize-space(.//span[@class='itemStore']/text())").get()),
#                 'Jail': product.xpath("normalize-space(.//div[@class='itemPrice  wide ']/text())").get()
            }