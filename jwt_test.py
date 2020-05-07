import jwt
import datetime

# 载荷中加入声明周期的概念
playload = {

    # 过期时间
    'exp':int((datetime.datetime.now() + datetime.timedelta(seconds=30)).timestamp()),
    'data':{'uid':2}
}

# 生成jwt
encode_jwt = jwt.encode(playload,'qwe123',algorithm='HS256')
# 转码
encode_str = str(encode_jwt,'utf-8')
# 解密
decode_jwt = jwt.decode(encode_str,'que123',algorithms=['HS256'])
print(encode_srt)
print(decode_jwt)
