from urllib import response
import scrapy
from .. items import QuotesprojectItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    # start_urls = [
    #     'https://quotes.toscrape.com/'
    # ]
    start_urls = [
        'https://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response):
        all_div_quotes = response.css('div.quote')
        items = QuotesprojectItem()
        for quotes in all_div_quotes:

            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items

        # next_page = response.css('li.next a::attr(href)').get()

        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)

        next_page = 'https://quotes.toscrape.com/page/' + str(QuoteSpider.page_number) + '/'

        if QuoteSpider.page_number < 11:
            QuoteSpider.page_number +=1
            yield response.follow(next_page, callback=self.parse)