from django.shortcuts import render
from login.models import Users
from login.forms import UserForm
from django.http import HttpResponseRedirect


def register(request):
    return render(request, 'register.html', {"Verification_code": "123456"})


def register_action(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            tel = uf.cleaned_data['inputTel']
            pwd = uf.cleaned_data['inputPassword']
            Users.objects.create(userMail=tel, userPwd=pwd)
            user = Users.objects.filter(userMail=tel, userPwd=pwd)
            if user:
                response = HttpResponseRedirect('/index/')
                response.set_cookie('user', tel, 3600)
                session_user = Users.objects.get(userTel=tel)
                request.session['userTel'] = session_user.userTel
                request.session['userName'] = session_user.userName
                return render(request, 'address.html')
            else:
                return render(request, 'register.html')
    else:
        return render(request, 'register.html')



