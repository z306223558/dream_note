from django.apps import AppConfig


class BookConfig(AppConfig):
    name = 'book'
    verbose_name = '小说管理'

    def ready(self):
        import book.receivers
