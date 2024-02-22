"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("empreq/",views.emp),
    path("haireq/",views.hai),
    path("haivars/",views.hai_vars),
    path("welreq/",views.wel),
    path("Homereq/",views.Home),
    path("test1req/",views.test1),
    path("home/",views.test2),
    path("susform/",views.test3),
    path("fform/",views.test4),
    path("login/",views.login),
    path("lform/",views.form_submit,name='form_submit'),
    path("test_for/",views.test_for),
     path("fempty/",views.test_for_empty),
    path("test_for2/",views.test_for_secondex),
    path("empDetails",views.emp_Details),
    path("test_two_same_objs/",views.test_two_same_objs),
    path("productDetails",views.product_Details),
    path("deptDetails",views.dept_Details),
    path("deptreq/<dname>/<dno>/<dlocation>/",views.dept),
    path("Big/",views.Big),
    path("iform/",views.iform),
    path("myform/",views.form_submit2,name='form_submit2'),
    path("product/",views.Product_insert),
    path('admin/', admin.site.urls),
   
]
