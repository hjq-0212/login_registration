from django.shortcuts import render,HttpResponse
from django import views
from app import models
import pymysql
from django.db import connection


def index(request):  #首页加登录功能
    if request.method =='GET':
        return render(request, 'index.html')
    else:
        account =request.POST.get('account')
        password = request.POST.get('password')
        yzm =request.POST.get('yzm')
        print(account,password,yzm)
        try:
            a =models.user_info.objects.get(account=account,password=password)
        except:
            return HttpResponse('用户名或者密码错误')

        else:
            return HttpResponse('登录成功')



def register(request):   #注册
    if request.method =='GET':
        return render(request, 'register.html')
    else:
        account =request.POST.get('account')
        email =request.POST.get('email')
        password1 =request.POST.get('password1')
        password2 = request.POST.get('password2')
        zym =request.POST.get('yzm')
        print(account,email,password1,password2,zym)

        if zym =='0glj':
            if password1 ==password2:
                # db =pymysql.connect('localhost','root','root','chitong')
                cursor =connection.cursor()
                sql=("insert into app_user_info(account,email,password) values ('%s','%s','%s')" %(account,email,password1))
                cursor.execute(sql)
                cursor.close()
                return render(request, 'index.html')
            else:
                print('账号密码不一致')
                return HttpResponse('账号密码不一致')
        else:
            print('验证码错误')
            return HttpResponse('验证码错误')





def password(request):
    return render(request,'password.html')

def change_password(request):
    return  render(request,'change_password.html')

def hanjingqian(request):
    pass

# class register1(views.View):
#     def get(self,request):
#         return render(request,'')
#     def post(self,request):

