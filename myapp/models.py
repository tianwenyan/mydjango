from django.db import models

# 导入时间域
from django.utils import timezone

# 基类
class Base(models.Model):
    # 创建时间字段
    create_time = models.DateTimeField(default=timezone.now,null=True)

    class Meta:
        abstract = True

# 商品类别表
class Category(Base):
    name = models.CharField(max_length=200)
    
    

    class Meta:
        db_table = 'category'

# 商品表
class Goods(Base):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    video = models.CharField(max_length=200)
    price = models.IntegerField()
    # 规格
    params = models.CharField(max_length=200)
    # 关注数
    flows = models.IntegerField(default=0,null=True)
    cid = models.IntegerField(default=0,null=True)

    class Meta:
        db_table = 'goods'

# 轮播图
class Carousel(Base):
    name = models.CharField(max_length=200)
    src = models.CharField(max_length=200)
    img = models.CharField(max_length=200)

    # 声明表名
    class Meta:
        db_table = 'carousel'


# 用户表
class User(Base):
    # 用户名
    username = models.CharField(max_length=200)

    # 密码
    password = models.CharField(max_length=200)

    # 头像
    img = models.CharField(max_length=200)

    #用户类别 0普通用户 1超级管理员 2.网站编辑 3.新浪
    type = models.IntegerField(default=0,null=0)

    # 手机号
    phone = models.CharField(max_length=200)

    # 个人主页统计
    num = models.IntegerField(default=0,null=True)

    # 声明表名
    class Meta:
        db_table = 'user'