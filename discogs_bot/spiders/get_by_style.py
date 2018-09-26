# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class GetByStyleSpider(scrapy.Spider):
    name = 'get_by_style'
    allowed_domains = ['discogs.com']
    start_urls = ['https://discogs.com/search/?genre_exact=Rock&type=release']

    def parse(self, response):
        links = response.xpath('//*[contains(@class, "card card_large")]/h4/a/@href').extract()
        for link in links:
            # Remove artists and bands from 'Releases'
            if 'artist' not in link:
                album_link = 'http://www.discogs.com' + link
                yield{'Album': album_link}

        next_url = response.xpath('//*[contains(@rel, "next")]/@href').extract_first()
        absolute_next_url = 'http://discogs.com/' + next_url
        yield Request(absolute_next_url, callback=self.parse)
