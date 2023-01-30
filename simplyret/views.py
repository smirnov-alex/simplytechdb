from django.shortcuts import render
from .forms import ConnectionForm, CheckingForm
from .simply import check_calibration_BS, upload_unique_id_BS, check_uniqueid, set_ret_on_BS
from .create_script import create_script_mos

RET_LIST_GLOBAL = []


def main(request):
    bs = ''
    form = ConnectionForm(request.POST or None)
    context = {'form': form, 'bs': bs}
    return render(request, 'simplyret/index.html', context)


def check_calibration(request):
    bs = request.POST.get("bs")
    login = request.POST.get("login")
    password = request.POST.get("password")
    server = request.POST.get("server")
    RET_list = check_calibration_BS(bs, login, password, server)
    context = {'login': login, 'password': password, 'bs': bs, 'server': server, 'RET_list': RET_list}
    return render(request, 'simplyret/check-calibration.html', context)


def upload_unique_id(request):
    bs = request.POST.get("bs")
    login = request.POST.get("login")
    password = request.POST.get("password")
    server = request.POST.get("server")
    RET_list = upload_unique_id_BS(bs, login, password, server)
    global RET_LIST_GLOBAL
    RET_LIST_GLOBAL = RET_list
    # add download file
    context = {'login': login, 'password': password, 'bs': bs, 'server': server, 'RET_list': RET_list}
    return render(request, 'simplyret/upload-unique-id.html', context)


def create_script(request):
    RET_list = RET_LIST_GLOBAL
    i = 1
    for item in RET_list:
        item.append(request.POST.get(f"tech_{i}"))
        item.append(request.POST.get(f"tilt_{i}"))
        i += 1
    bs = request.POST.get("bs")
    result = create_script_mos(bs, RET_list)
    form = ConnectionForm(request.POST or None)
    context = {'bs': bs, 'RET_list': RET_list, 'form': form, 'result': result}
    return render(request, 'simplyret/create-script.html', context)


def check_current(request):
    form = CheckingForm(request.POST or None)
    context = {'form': form}
    return render(request, 'simplyret/check-current.html', context)


def upload_current(request):
    bs = request.POST.get("bs")
    RET_list = check_uniqueid(bs)
    global RET_LIST_GLOBAL
    RET_LIST_GLOBAL = RET_list
    context = {'bs': bs, 'RET_list': RET_list}
    return render(request, 'simplyret/upload-current.html', context)


def set_ret(request):
    bs = request.POST.get("bs")
    login = request.POST.get("login")
    password = request.POST.get("password")
    server = request.POST.get("server")
    result = set_ret_on_BS(bs, login, password, server)
    context = {'login': login, 'password': password, 'bs': bs, 'server': server, 'result': result}
    return render(request, 'simplyret/set-ret.html', context)
