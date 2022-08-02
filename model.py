import datetime

import peewee
from lib.database import db


class Category(db.Model):
    name = peewee.CharField()
    slug = peewee.CharField()
    class Meta:
        table_name = "category"

class Post(db.Model):
    title = peewee.CharField()
    slug = peewee.CharField(index=True, max_length=100)
    category = peewee.ForeignKeyField(Category, backref='posts')
    content = peewee.TextField()
    readnum = peewee.IntegerField(default=0)
    tags = peewee.CharField(null=True)
    slug = peewee.CharField(null=True)
    created = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        table_name = "posts"
        order_by = ('-created',)

