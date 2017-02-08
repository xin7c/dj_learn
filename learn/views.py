#coding:utf-8
from django.shortcuts import render

from django.http import HttpResponse

def index(req):
    print "===app/index.html==="
    # print req.get_host()
    # print req.method

    # for i in req.META.items():
    #     print i

    get_items = req.GET.items()
    post_items = req.POST.items()
    REMOTE_ADDR = req.META["REMOTE_ADDR"]
    HTTP_USER_AGENT = req.META["HTTP_USER_AGENT"]

    print "Connect From:", REMOTE_ADDR
    print "请求参数:", get_items
    #context数据构造
    context = {}
    context["get_host"] =req.get_host()
    context["method"] = req.method
    context["get_items"] = get_items
    context["post_items"] = post_items
    context["REMOTE_ADDR"] = REMOTE_ADDR
    context["HTTP_USER_AGENT"] = HTTP_USER_AGENT
    return render(req, "learn/index.html", context=context)


