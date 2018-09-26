# -*- coding: utf-8 -*-
import scrapy


class GetByStyleSpider(scrapy.Spider):
    name = 'get_by_style'
    allowed_domains = ['discogs.com/search/?genre_exact=Rock&type=release']
    start_urls = ['http://discogs.com/search/']

    def parse(self, response):
        links = response.xpath('//*[contains(@class, "card card_large")]/h4/a/@href').extract()
        for link in links:
            # Remove artists and bands from 'Releases' (as they aren't albums...)
            if 'artist' not in link:
                yield{ 'link': link}