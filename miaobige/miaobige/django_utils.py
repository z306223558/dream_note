# coding=utf-8
from book.models import BookCategory, Author, Book


class DjangoModelUtils(object):

    @staticmethod
    def add_category_info(cate_name):
        return BookCategory.objects.create(name=cate_name)

    @staticmethod
    def check_category_exist(cate_name):
        return BookCategory.objects.filter(name=cate_name).first()

    @staticmethod
    def check_author_exist(author_name):
        return Author.objects.filter(name=author_name).first()

    @staticmethod
    def add_author_info(author_name):
        return Author.objects.create(name=author_name)

    def save_book(self, item):
        author_info = self.check_author_exist(item['author'])
        if not author_info:
            author_info = self.add_author_info(item['author'])

        # 分类
        category_info = self.check_category_exist(item['category'])
        if not category_info:
            category_info = self.add_category_info(item['category'])

        Book.objects.create(name=item['name'],
                            author=author_info,
                            category=category_info,
                            note_count=item['note_count'],
                            char_count=item['char_count'],
                            thumb=item['thumb'],
                            status=item['status'],
                            description=item['description'],
                            source_id=item['book_id'],
                            source_website='m.bxwxorg.com')
