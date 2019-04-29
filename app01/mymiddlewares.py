#!/Users/liangyufeng/venv/bin/python3
# _*_ coding:utf-8 _*_
import re

from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

# 中间件版登录认证
from homework01 import settings


class Auth(MiddlewareMixin):

    def process_request(self, request):
        # 获取当前访问的页面
        url = request.path_info
        # 白名单
        for i in settings.WHITE_LIST:  # 循环是为了admin开头的路径的访问
            if re.match(i, url):
                return

        # 不在白名单中就要进行登录验证
        is_login = request.session.get('is_login', False)
        if is_login:  # 经过了登录认证,正常执行下面的流程
            pass  # 或者 return None是一样的效果
        else:  # 否则就要重定向到登录页面先成功登录
            return redirect(reverse('login'))
