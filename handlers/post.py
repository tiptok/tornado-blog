from handlers import BaseHandler
from model import Post
import json
from playhouse.shortcuts import model_to_dict,dict_to_model
from middleware import middlewares

class PostHandler(BaseHandler):
    async def get(self,id=None):
        if id=='':
            lt = int(self.get_argument("limit"))
            p = Post.select().limit(lt)
            posts = []
            for post in p:
                posts.append({'title':post.title,'content':post.content})
            self.write(json.dumps(posts))
            return
        try:
            p = Post.get(id=id)
            dictPost = model_to_dict(p)
            dictPost.pop('created')
            # print(model_to_dict(p,exclude= ['created']))
            self.write(json.dumps(dictPost))
        except Exception as e:
             print(e)
    def delete(self,id):
        self.write("blog delete " + id)
    def put(self,id):
        data = json.loads(self.request.body)
        self.write("blog put %s  %s" % (id,data["id"]))  
    def post(self,id=None):
       data = json.loads(self.request.body)
       self.write("blog post %s" % json.dumps(data))
routers = [
    ## post
    (r'/blog/([^/]*)',PostHandler,dict(middleware=middlewares())),
    ## delete get put
    (r'/blog/(.*)(\d+)',PostHandler,dict(middleware=middlewares())),
    ## list
    (r'/blog?(.*)',PostHandler,dict(middleware=middlewares()))    
]        