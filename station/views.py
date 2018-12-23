from django.shortcuts import render
from django.db import connection


def index(request, cs_add=None):
    cs_add_state = CsAddState()
    cs_add_state.__init__()
    if cs_add is not None:
        cs_add_state.cs_add = cs_add
    cursor = connection.cursor()
    sql = "select station_cs.* ,station_usercs.* from station_cs left join station_usercs on station_cs.csId =station_usercs.csId_id "
    cursor.execute(sql)
    css = cursor.fetchall()
    print(css)
    return render(request, 'ListCS.html', {"css": css, "csAddState": cs_add_state, "userTel": request.session["userTel"]})


def to_reset(request):
    return render(request, 'reset.html')





def show_common(request, cs_add=None):
    cs_add_state = CsAddState()
    cs_add_state.state = 1
    cs_add_state.cs_add = cs_add
    cursor = connection.cursor()
    if cs_add is not None:
        address = "博文苑"+cs_add.__str__()+"号楼"
        sql = "select station_cs.* ,station_usercs.* from station_cs left join station_usercs on station_cs.csId =station_usercs.csId_id where station_cs.csAdd ='"+address+"'"
        cursor.execute(sql)
        css = cursor.fetchall()
        print(css)
    else:
        sql = "select station_cs.* ,station_usercs.* from station_cs left join station_usercs on station_cs.csId =station_usercs.csId_id "
        cursor.execute(sql)
        print(sql)
        css = cursor.fetchall()
        print(css)
    userTel = request.session["userTel"];
    return render(request, 'ListCS.html', {"css": css, "csAddState": cs_add_state, "userTel": userTel})


def show_free(request, cs_add=None):
    cs_add_state = CsAddState()
    cs_add_state.state = 2
    cs_add_state.cs_add = cs_add
    cursor = connection.cursor()
    if cs_add is not None:
        address = "博文苑" + cs_add.__str__() + "号楼"
        sql = "select station_cs.* ,station_usercs.* from station_cs left join station_usercs on station_cs.csId =station_usercs.csId_id where station_cs.csStates = 1 and station_cs.csAdd ='" + address + "'"
        cursor.execute(sql)
        css = cursor.fetchall()
        print(css)
    else:
        sql = "select station_cs.* ,station_usercs.* from station_cs left join station_usercs on station_cs.csId =station_usercs.csId_id where station_cs.csStates = 1"
        cursor.execute(sql)
        css = cursor.fetchall()
        print(css)
    userTel = request.session["userTel"];
    return render(request, 'ListCS.html', {"css": css, "csAddState": cs_add_state, "userTel": userTel})


def show_focus(request, cs_add=None):
    cs_add_state = CsAddState()
    cs_add_state.state = 3
    cs_add_state.cs_add = cs_add
    cursor = connection.cursor()
    if cs_add is not None:
        address = "博文苑" + cs_add.__str__() + "号楼"
        sql = "select station_cs.* ,station_usercs.* from station_cs left join station_usercs on station_cs.csId =station_usercs.csId_id where station_usercs.userTel_id = " + \
              request.session["userTel"]+" and station_cs.csAdd = '" + address + "'"
        cursor.execute(sql)
        css = cursor.fetchall()
        print("我按照地址拆线呢了")
    else:
        sql = "select station_cs.* ,station_usercs.* from station_cs left join station_usercs on station_cs.csId =station_usercs.csId_id where station_usercs.userTel_id = " + \
              request.session["userTel"]
        cursor.execute(sql)
        css = cursor.fetchall()
        print("什么地址")
    print(css)
    userTel = request.session["userTel"];
    return render(request, 'ListCS.html', {"css": css, "csAddState": cs_add_state, "userTel": userTel})


def change_state(request):
    if request.POST:
        if 'update' in request.POST:
            cs_id = request.POST.get("num")
            cs_add = request.POST.get("cs_add")
            cursor = connection.cursor()
            sql = "insert into station_usercs ( csId_id,userTel_id ) values ("+cs_id+","+request.session["userTel"]+")"
            print(sql)
            cursor.execute(sql)
        else:
            cs_id = request.POST.get("num")
            cs_add = request.POST.get("cs_add")
            cursor = connection.cursor()
            sql = "delete from station_usercs where csId_id = " + cs_id + " and userTel_id = " + request.session[
                "userTel"]
            cursor.execute(sql)
    return index(request, cs_add)


class CsAddState(object):
    def __init__(self):
        self.state = 1
        self.cs_add = 6
