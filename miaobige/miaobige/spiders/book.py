# -*- coding: utf-8 -*-
import re
from abc import ABC

import scrapy
from scrapy.http import Request

from miaobige.django_utils import DjangoModelUtils
from miaobige.items import BookItem, AuthorItem, CategoryItem
from book.models import Author
from miaobige.pipelines import DjangoPipeline


class BookSpider(scrapy.spiders.CrawlSpider):

    name = 'book'
    allowed_domains = ['bxwxorg.com']

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

    def parse_book(self, response):
        book = BookItem()
        details = response.xpath('//*[@id="info"]/div[2]/div[2]//text()')
        book['thumb'] = response.xpath('//*[@id="info"]/div[2]/div[2]/img')[0].attrib['src']
        book['name'] = details[2].root

        book['author'] = details[5].root
        book['category'] = details[7].root
        if not DjangoModelUtils.check_category_exist(details[7].root):
            DjangoModelUtils.add_category_info(details[7].root)

        book['note_count'] = 0
        book['char_count'] = self.parse_char_count(details[10].root)
        book['like_count'] = 0
        book['click_count'] = 0
        book['status'] = self.parse_status_info(details[8].root)

        # 简介
        book['description'] = self.parse_description(response.xpath('//*[@id="info"]/div[2]/div[3]/div[2]').xpath('string(.)').extract()[0], details[2].root)
        book['book_id'] = self.parse_id(response.url)

        if not DjangoModelUtils.check_author_exist(details[5].root):
            yield Request(self.author_base_url.format(details[5].root), self.parse_author)
        yield book

    @staticmethod
    def add_author_info(author_name):
        return Author.objects.create(name=author_name)

    @staticmethod
    def parse_char_count(char_count):
        return char_count.replace('万字', '')

    @staticmethod
    def parse_description(content, book_name='', desc_type='book'):
        if desc_type == 'book':
            return content.replace('最新章节{}全文阅读推荐地址：https://m.bxwxorg.com/book/1.htmlcambrian.render(\'body\')'.format(book_name), '')
        else:
            return content.replace('如果您在笔下文学阅读耳根作品时，遇到问题，请及时反馈，我们将第一时间解决，争取为您奉上愉快的阅读体验!', '')

    @staticmethod
    def parse_status_info(status_info):
        return 2 if status_info == '连载中' else 3

    @staticmethod
    def parse_id(url):
        return re.search(r'\d+', url).group()

    def parse_author(self, response):
        print("enter into author")
        author = AuthorItem()
        author['name'] = response['meta']['author_name']
        author['description'] = self.parse_description(response.xpath('/html/body/div[2]/div[1]/div[2]').xpath('string(.)').extract(), '', 'author')
        yield author

