# coding=utf-8
from django.db import models
from book.constants import BookStatus, AuthorStatus


class Book(models.Model):
    name = models.CharField(verbose_name="书名", max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, verbose_name="作者", related_name='books', blank=True, null=True)
    category = models.ForeignKey('BookCategory', on_delete=models.SET_NULL, verbose_name="作品分类", related_name='books', blank=True, null=True)
    note_count = models.IntegerField(verbose_name='章节数', default=0)
    char_count = models.IntegerField(verbose_name='总字数', default=0)
    like_count = models.IntegerField(verbose_name='收藏数', default=0)
    click_count = models.IntegerField(verbose_name="点击数", default=0)
    thumb = models.ImageField(verbose_name="封面图", upload_to='', default='', null=True, blank=True)
    status = models.PositiveSmallIntegerField(verbose_name="书籍状态", choices=BookStatus.BOOK_STATUS_CHOICE, default=BookStatus.AUDITING)
    description = models.TextField(verbose_name='书籍简介', default='', null=True, blank=True)
    source_id = models.IntegerField(verbose_name='来源ID', default=0, blank=True, null=True)
    source_website = models.CharField(verbose_name="来源站点", max_length=200, default='', blank=True, null=True)
    created = models.DateTimeField(verbose_name="创建时间", auto_created=True, auto_now_add=True)
    updated = models.DateTimeField(verbose_name="更新时间", auto_created=True, auto_now=True)


class Author(models.Model):
    name = models.CharField(verbose_name="作者名称", max_length=200, unique=True)
    description = models.TextField(verbose_name='书籍简介', default='', null=True, blank=True)
    like_count = models.IntegerField(verbose_name='收藏数', default=0)
    status = models.PositiveSmallIntegerField(verbose_name="作者状态", choices=AuthorStatus.AUTHOR_STATUS_CHOICE,
                                              default=AuthorStatus.AUDITING)
    created = models.DateTimeField(verbose_name="创建时间", auto_created=True, auto_now_add=True)
    updated = models.DateTimeField(verbose_name="更新时间", auto_created=True, auto_now=True)


class Note(models.Model):
    note_title = models.CharField(verbose_name="章节名", max_length=255, default='')
    note_sort = models.IntegerField(verbose_name="章节数", default=0, blank=True, null=True)
    content = models.TextField(verbose_name="章节内容", default='', blank=True, null=True)
    char_count = models.IntegerField(verbose_name='总字数', default=0)
    created = models.DateTimeField(verbose_name="创建时间", auto_created=True, auto_now_add=True)
    updated = models.DateTimeField(verbose_name="更新时间", auto_created=True, auto_now=True)


class BookCategory(models.Model):
    name = models.CharField(verbose_name="分类名称", max_length=200, unique=True)
    description = models.TextField(verbose_name='分类简介', default='', null=True, blank=True)
    thumb = models.ImageField(verbose_name="封面图", upload_to='', default='', null=True, blank=True)
    created = models.DateTimeField(verbose_name="创建时间", auto_created=True, auto_now_add=True)
    updated = models.DateTimeField(verbose_name="更新时间", auto_created=True, auto_now=True)

