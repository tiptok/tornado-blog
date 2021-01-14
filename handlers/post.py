from handlers import BaseHandler
from model import Post
import json
from playhouse.shortcuts import model_to_dict,dict_to_model

class PostHandler(BaseHandler):
    async def get(self,id=None):
        if id=='':
            p = Post.select().limit(10) #.limit(1)
            posts = []
            for post in p:
                posts.append({'title':post.title,'content':post.content})
            self.write(json.dumps(posts))
            return
        p = Post.get(id=id)   
        dictPost = model_to_dict(p)
        dictPost.pop('created')
        # print(model_to_dict(p,exclude= ['created'])) 
        self.write(json.dumps(dictPost))    
    def delete(self,id):
        self.write("blog delete " + id)
    def put(self,id):
        self.write("blog put " + id)  
    def post(self):
        p = Post.select().limit(10) #.limit(1)
        posts = []
        for post in p:
            posts.append({'title':post.title,'content':post.content})
        self.write(json.dumps(posts))

routers = [
    (r'/blog/([^/]*)',PostHandler),
    (r'/blog/(\d+)',PostHandler)
]        