from django.shortcuts import render,redirect
#导包
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
#导入类视图
from django.views import View


import json
from django.core.serializers import serialize
from rest_framework.response import Response
from rest_framework.views import APIView
#导入加密库
import hashlib
#导入图片库
#绘画库
from PIL import ImageDraw
#字体库
from PIL import ImageFont
#图片库
from PIL import Image
#随机库
import random
#文件流
import io

import requests

#导入上传文件夹配置
from mydjango.settings import UPLOAD_ROOT
import os

#导入原生sql模块
from django.db import connection

import jwt

#导入redis数据库
import redis

#导入时间模块
import time

#导入公共目录变量
from mydjango.settings import BASE_DIR

#导包
from django.db.models import Q,F

#导入dwebsocket的库
from dwebsocket.decorators import accept_websocket
import uuid

from myapp.models import User
import re

# md5加密
def myapp_password(mypass):

    # 生成MD5对象
    md5 = hashlib.md5()

    # 转码
    mypass_utf8 = str(mypass).encode(encoding='utf-8')

    # 加密操作
    md5.update(mypass_utf8)

    return md5.hexdigest()

# 登陆接口
class Login1(APIView):
	def get(self,request):

		# 接收参数 
		username = request.GET.get('username',None)
		password = request.GET.get('password',None)

		# 查询数据
		user = User.objects.filter(username=username,password=myapp_password(password)).first()

		if user:
			return Response({'code':200,'message':'登陆成功','uid':user.id,'username':user.username})
		
		else:
			return Response({'code':403,'message':'您的用户名或密码错误,请重新输入'})


# 注册接口
class Register1(APIView):

	def get(self,request):

		#接收参数  
		username = request.GET.get('username','null')
		password = request.GET.get('password','null')

        
		
		#排重
		user = User.objects.filter(username=username).first()

		if user:
			res = {}
			res['code'] = 405
			res['message'] = '该用户名已存在'
			return Response(res)

		#入库
		user = User(username=username,password=myapp_password(password))
		user.save()

		res = {}
		res['code'] = 200
		res['message'] = '恭喜，注册成功'

		return Response(res)
 