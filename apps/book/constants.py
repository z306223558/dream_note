# coding=utf-8


class BookStatus:

    AUDITING = 1
    SERIALIZED = 2
    FINISH = 3
    BAN = 4

    BOOK_STATUS_CHOICE = [
        (AUDITING, '审核中'),
        (SERIALIZED, '连载中'),
        (FINISH, '完本'),
        (BAN, '下架')
    ]


class AuthorStatus:

    AUDITING = 1
    NORMAL = 2
    BAN = 3

    AUTHOR_STATUS_CHOICE = [
        (AUDITING, '审核中'),
        (NORMAL, '正常'),
        (BAN, '下架')
    ]