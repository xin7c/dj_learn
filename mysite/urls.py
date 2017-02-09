"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from learn import views as learn_views
from docs import views as docs_views
from django.contrib.auth import urls as auth_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', learn_views.index, name='aha'),
    url(r'^doc/$', docs_views.doc, name='doc'),
    url(r'^doc/add/$', docs_views.add, name='add'),
    url(r'^doc/myForms/$', docs_views.myForms, name='myForms'),
    url(r'^send_mail/$', learn_views.send_mail_result, name='send_mail'),
    # url(r'^send_mail/send_mail_result$', learn_views.send_mail_result, name='send_mail_result'),
    # url(r'^accounts/', include(auth_urls, namespace='accounts')),

]