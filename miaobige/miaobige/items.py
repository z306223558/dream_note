# -*- coding: utf-8 -*-
import scrapy


class BookItem(scrapy.Item):

    name = scrapy.Field()
    author = scrapy.Field()
    note_count = scrapy.Field()
    char_count = scrapy.Field()
    like_count = scrapy.Field()
    click_count = scrapy.Field()
    thumb = scrapy.Field()
    status = scrapy.Field()
    description = scrapy.Field()
    book_id = scrapy.Field()


class AuthorItem(scrapy.Item):

    name = scrapy.Field()
    description = scrapy.Field()
    author_id = scrapy.Field()


class NoteItem(scrapy.Item):

    note_title = scrapy.Field()
    note_sort = scrapy.Field()
    content = scrapy.Field()
    char_count = scrapy.Field()
    click_count = scrapy.Field()


class CategoryItem(scrapy.Item):

    name = scrapy.Field()
    description = scrapy.Field()


