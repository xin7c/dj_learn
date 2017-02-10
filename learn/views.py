#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.mail import mail_admins, mail_managers

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

def send_mail():
    """发邮件模块"""
    print "send_mail:Start..."
    from_email = settings.DEFAULT_FROM_EMAIL
    static_dir = settings.STATICFILES_DIRS
    # subject 主题, content 内容, from_email, to_addr 收件人列表
    msg = EmailMultiAlternatives(u'Django 测试邮件', u'十个凯文九个Gay',
                                 from_email, ['xuchu@acfun.tv'])
    msg.content_subtype = "html"
    # 添加附件（可选）
    # print static_dir[0]
    # img_path = static_dir[0] + '/girl01.png'
    # msg.attach_file(img_path)
    # 发送
    msg.send()
    # mail_managers(u'发送成功', u'已发送哦', fail_silently=True)
    # return HttpResponse(u"Send Mail Successed!")
    print "send_mail:Done..."


def send_mail_result(req):
    lenParam = len(req.GET.items())
    keysParam = req.GET.keys()
    print keysParam
    # print req.GET['a']
    if lenParam == 0:
        print "Data is None!"
        # return HttpResponse(u"Data is None!")
        return render(req, "learn/send_mail_result.html",
                      context={"send_mail_result": "Data is None!"})

    elif "a" in keysParam and req.GET['a'] != '1':
        print "Send Mail Failed!"
        # return HttpResponse(u"Send Mail Failed!")
        return render(req, "learn/send_mail_result.html",
                      context={"send_mail_result": "Data is Failed!"})

    elif "a" in keysParam and req.GET['a'] == '1':
        print "send_mail_result"
        send_mail()
        # return HttpResponse(u"Send Mail Successed!")
        return render(req, "learn/send_mail_result.html",
                      context={"send_mail_result": "Data is Okkkkkkkkkkkkkkkkkkk!"})
    else:
        return render(req, "learn/send_mail_result.html",
                      context={"send_mail_result": "Data is a=xxx"})

def add(req):
    post_items = req.POST.items()
    print post_items
    return HttpResponse(post_items)

