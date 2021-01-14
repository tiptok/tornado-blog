import peewee
import datetime
from core import db

class Post(db.Model):
    title = peewee.CharField()
    slug = peewee.CharField(index=True, max_length=100)
    # category = peewee.ForeignKeyField(Category, related_name='posts')
    content = peewee.TextField()
    readnum = peewee.IntegerField(default=0)
    tags = peewee.CharField(null=True)
    slug = peewee.CharField(null=True)
    created = peewee.DateTimeField(default=datetime.datetime.now)

    # @cached_property
    # def prev(self):
    #     posts = Post.select().where(Post.created < self.created)\
    #         .order_by(Post.created)
    #     return posts.get() if posts.exists() else None

    # @cached_property
    # def next(self):
    #     posts = Post.select().where(Post.created > self.created)\
    #         .order_by(Post.created)
    #     return posts.get() if posts.exists() else None

    class Meta:
        table_name = "posts"
        order_by = ('-created',)