def Response(message = None,data = None,code = 0):
    return {
        "code":code,
        "msg":message,
        "data":data,
    }

def ResponseList(message = None,data = None,code = 0):
    total = 0
    if data is not None:
        total = len(data)
    else:
        data = []
    return {
        "code":code,
        "msg":message,
        "data":{
            "list":data,
            "total":total,
        },
    }