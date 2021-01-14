from lib import database
import redis

redis_server = redis.StrictRedis(host="127.0.0.1",port=6379,password='123456')
db = database.Database({'db':"MYSQL"})