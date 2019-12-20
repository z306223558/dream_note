# -*- coding: utf-8 -*-
# from apps.book.models import Book, Author, Note, BookCategory
from miaobige.items import *


class DjangoPipeline(object):

    def process_book(self, item):
        return item

    def process_note(self, item):
        return item

    def process_item(self, item, spider):
        '''
        if isinstance(item,ChaptersItem):
          self.process_ChaptersItem(item)
        '''
        if isinstance(item, BookItem):
            self.process_book(item)
        if isinstance(item, NoteItem):
            self.process_note(item)
        return item
