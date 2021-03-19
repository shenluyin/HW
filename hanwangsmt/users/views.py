from django.shortcuts import render

# Create your views here.
import re

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from users.models import User
# Create your views here.
from django.views import View



"""


判断用户名是否重复的功能

前端：当用户输入了用户名之后失去焦点 触发ajax请求

后端：
    请求：接收用户名 
    业务逻辑：根据用户名 查询数据库 如果查询数量等于0 说明没有注册
    响应 ： json数据{code： count：0/1，errmsg：ok}


"""





class UsernameCountView(View):

    def get(self, request, username):
        # pass
        # 对用户名进行判断
        # if not re.match('^[a-zA-Z0-9_-]{5,20}',name):
        #
        #     return JsonResponse({'code':200, 'errmsg':'用户名不满足需求'})

        # 查询
        count=User.objects.filter(username=username).count()
        # return JsonResponse({'code':0, 'count':count,'errmsg':'ok'})
        return JsonResponse({"code":0, "count":count,"errmsg":"ok"})




def register(request):

    return render(request, 'register.html')