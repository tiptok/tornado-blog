from model import Post,Category
import json
from playhouse.shortcuts import model_to_dict
from flask import Blueprint,request
from lib.log import logger
from lib.common import Response,ResponseList

app = Blueprint('post',__name__)

@app.route('/blog/<int:id>',methods=['GET'])
def blog_get(id=None):
    if id=='':
        return
    try:
        p = Post.get(id=id)
        dictPost = model_to_dict(p)
        dictPost.pop('created')
        # print(model_to_dict(p,exclude= ['created']))
        return json.dumps(dictPost)
    except Exception as e:
         print(e)

@app.route('/blog/<int:id>',methods=['DELETE'])
def blog_delete(id):
    Post.delete_by_id(id)
    return Response("blog delete %d" % id)

@app.route('/blog',methods=['POST'])
def blog_post(id=None):
   data = json.loads(request.data)
   post = Post(
       title = data['title'],
       content = data['content'],
       tags = data['tags'],
       category = data['categoryId'],
       channel=data['channel'],
   )
   post.save()
   return Response('save success %d' % post.id,model_to_dict(post))

@app.route('/blog/<int:id>',methods=['PUT'])
def blog_put(id):
    data = json.loads(request.data)
    try:
        post = Post.get(id=id)
        post.title = data['title']
        post.content = data['content']
        post.tags = data['tags']
        post.category = data['categoryId']
        post.channel = data['channel']
        post.save()
    except Exception as e:
       logger.error(e)
    # data = json.loads(request.data)
    return Response("blog put %s  %s" % (id,data['title']))