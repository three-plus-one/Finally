from django.http import HttpResponseRedirect
from django.shortcuts import render
from login.forms import UserForm, ResetForm
from login.models import Users


def login(request):
    return render(request, 'login.html')


def login_action(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            tel = uf.cleaned_data['inputTel']
            pwd = uf.cleaned_data['inputPassword']
            user = Users.objects.filter(userTel=tel, userPwd=pwd)
            if user:
                response = HttpResponseRedirect('/index/')
                response.set_cookie('user', tel, 3600)
                session_user = Users.objects.get(userTel=tel)
                request.session['userTel'] = session_user.userTel
                request.session['userName'] = session_user.userName
                request.session['userMail'] = session_user.userMail
                return HttpResponseRedirect('/map/')
            else:
                return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def to_un_reset(request):
    return render(request, 'un_reset.html')


def reset_pwd(request):
    print("*************233")
    if request.method == 'POST':
        uf = ResetForm(request.POST)
        if uf.is_valid():
            old_pwd = uf.cleaned_data['oldpaw1']
            new_pwd = uf.cleaned_data['newpaw1']
            user = Users.objects.filter(userTel=request.session['userTel'])
            print("*************1")
            if user.get(userPwd=old_pwd):
                Users.objects.update(userPwd=new_pwd)
                print("*************2")
                return HttpResponseRedirect('/map/')
            else:
                print("*************3")
                return render(request, 'reset.html')
    else:
        print("*************4")
        return render(request, 'reset.html')
    return render(request, 'reset.html')


def logout(request):
    del request.session["userTel"]
    del request.session["userName"]
    del request.session["userMail"]
    return render(request, 'login.html')
