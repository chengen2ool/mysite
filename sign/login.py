from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect,render_to_response
from django.http.response import JsonResponse
from tools import *
import os
os.environ.update({"DJANGO_SETTINGS_MODULE": "config.settings"})



def register(request):
    if request.method == 'POST' :
        username  = request.POST.get('username')
        password = request.POST.get('password')
        pwdagain = request.POST.get('pwdagain')
        if password == pwdagain :
            if signup_judge(username = username):
                if signup(username,password) :
                    request.session['username']=username
                    return redirect('/tool/index/')
                else:
                    return   render_to_response('signup.html')
            else :
                return render_to_response('signup.html',{'errormsg':'用户名已注册'})
        else :
            return render_to_response('signup.html',{'errormsg':'请输入相同密码'})
    return render_to_response('signup.html')

def login(request):
    if request.method == 'POST' :
        username  = request.POST.get('username')
        password = request.POST.get('password')
        if login_judge(username,password):
            request.session['username'] = username
            return redirect('/tool/interface/create/')
        else :
            return render_to_response('login.html',{'errormsg':'用户名密码错误'})
    return render_to_response('login.html')

def resetlogin(request):
    if request.method == 'POST' :
        username  = request.POST.get('username')
        password = request.POST.get('password')
        pwdagain = request.POST.get('pwdagain')
        if password == pwdagain :
            if signup_judge(username = username) is False:
                resetpwd(username,password)
                request.session['username']=username
                return redirect('/tool/index/')
            else :
                return render_to_response('reset.html',{'errormsg':'用户名不存在'})
        else :
            return render_to_response('reset.html',{'errormsg':'请输入相同密码'})
    return render_to_response('reset.html')	