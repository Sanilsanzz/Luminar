from django.urls import path,include
from testapp import views


urlpatterns=[
    path("test1/",views.test1,name="test1"),
    path("form1/",views.form1,name="form1"),
    path("saver2/", views.saver2, name="saver2"),
    path("display1/",views.display1,name="display1"),
    path("edit1/<int:dataid>",views.edit1,name="edit1"),
    path("update11/<int:dataid>",views.update1,name="update1"),
    path("delete1/<int:dataid>",views.delete1,name="delete1"),








]