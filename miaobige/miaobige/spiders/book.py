# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from miaobige.items import BookItem, AuthorItem
from apps.book.models import Author


class BookSpider(scrapy.Spider):

    name = 'book'
    allowed_domains = ['https://m.bxwxorg.com/']

    def __init__(self):
        self.format_url = '//m.bxwxorg.com/book/{}.html'
        self.author_base_url = 'https://m.bxwxorg.com/author/{}.html'
        self.urls = self.get_urls()
        self.default_url = 'https://m.bxwxorg.com/'
        super().__init__()

    def get_urls(self):
        return [self.format_url.format(i) for i in range(1, 2)]

    def start_requests(self):

        for url in self.urls:
            url = 'https:' + url
            yield Request(url, self.parse_book)
        # yield Request(self.default_url, self.parse)

    def parse(self, response):
        print("生成抓取链接成功")

    def parse_book(self, response):
        book = BookItem()
        details = response.xpath('//*[@id="info"]/div[2]/div[2]//text()')
        book['thumb'] = response.xpath('//*[@id="info"]/div[2]/div[2]/img')[0].attrib['src']
        book['name'] = details[2].root
        author_name = details[5].root
        if not self.check_author_exist(author_name):
            author_info = yield Request(self.author_base_url.format(author_name), self.parse_author)
        book['name'] = details[2].root
        book['name'] = details[2].root
        book['name'] = details[2].root
        book['name'] = details[2].root
        book['name'] = details[2].root

    def parse_author(self, response):
        print("enter into author")
        author  = AuthorItem()
        author['name'] = '耳根'
        author['description'] = '耳根123123'
        yield author

    @staticmethod
    def check_author_exist(author_name):
        # TODO 存入redis可以直接拿到生成的key
        return Author.objects.filter(name=author_name).first()