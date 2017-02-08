"""ask URL Configuration

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
# from django.contrib import admin
from ask.views import test, my_test
from qa.views import questions_main_newer, questions_popular, question_viewer, feedback


urlpatterns = [
    # url(r'^admin/', admin.site.urls),

    url(r'^$', questions_main_newer),
    url(r'^popular/', questions_popular),
    url(r'^question/(?P<id_question>\d+)/$', question_viewer),


    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^ask/', test),
    url(r'^new/', test),

    url(r'^my/(\d+)$', my_test),
    url(r'^my2/(?P<pk>\d+)$', my_test),
    url(r'feedback/$', feedback),
]
