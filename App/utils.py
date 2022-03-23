import uuid, base64

from flask import request, session

def check_token(fun):
    def wrapper(*args, **kwargs):
        # token = request.headers.get("token")

        # user_id = get_user_id(token)

        # if not user_id:
        #     return {
        #                "success": False,
        #                "remark": "用户未登录",
        #            }, 401

        return fun(*args, *kwargs)

    return wrapper


def generate_token(prefix=''):
    token = prefix + uuid.uuid4().hex
    return token


def get_user_id(token):
    if token:
        return session.get(token) or ''
    return ''

def b64decode_(v):
    try:
        return base64.b64decode(v).decode()
    except:
        #网页传来的base64内容,在被flask捕捉的时候,加号会被解码成空格,导致解码报错
        #这个bug调了我半个小时,我还以为前端js生成的base64有问题,fuck
        return base64.b64decode(v.replace(' ','+')).decode()

def b64encode_(v):
    return base64.b64encode(v.encode()).decode()