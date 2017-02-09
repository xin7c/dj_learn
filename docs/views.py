# coding:utf-8
from django.shortcuts import render
from learn.models import User  # 试验model查询数据库
from django.http import HttpResponse

def doc(req):
    get_items = req.GET.items()
    user_mysql_all = User.objects.all()  # 试验model查询数据库
    # context数据构造
    context = {}
    context["get_items"] = get_items
    context["user_mysql_all"] = user_mysql_all  # 试验model查询数据库

    return render(req, "docs/doc.html", context=context)


def add(req):
    REMOTE_ADDR = req.META["REMOTE_ADDR"]
    get_items = req.GET.items()
    post_items = req.POST.items()
    # context数据构造
    context = {}
    context["method"] = req.method
    context["get_items"] = get_items
    context["post_items"] = post_items
    context["REMOTE_ADDR"] = REMOTE_ADDR
    return render(req, "docs/add.html", context=context)

# 引入我们创建的表单类
from .forms import AddForm
def myForms(req):
    if req.method == 'POST':# 当提交表单时
        form = AddForm(req.POST) # form 包含提交的数据
        if form.is_valid():# 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:# 当正常访问时
        form = AddForm()
    return render(req, 'docs/myForms.html', {'form': form})
