from django.conf.urls import url
from visiter import views
from django.views.generic import ListView,DetailView
from visiter.models import Member
urlpatterns=[
   
    url(r'^$', views.index, name="index"),
    url(r'^about/', views.about, name="about"),
    url(r'^contact/', views.contact, name="contact"),
    url(r'^login/', views.login, name="login"),
    url(r'^register/', views.register, name="register"),
    url(r'^checkLogin/', views.checkLogin, name="checkLogin"),
     url(r'^profile/', views.checkLogin, name="profile"),
    url(r'^logout/', views.logout, name="logout"),
    url (r'^addBus/',views.addBus,name="addBus"),
    url (r'^category/',views.category,name="category"),
    #url (r'^prof/',views.prof,ListView.as_view(queryset=Member.objects.get(),template_name='prof.html')),
    #url (r'^prof/',views.prof,ListView.as_view(queryset=Member.objects.get(name=request.session,),template_name='prof.html'),
    url (r'^prof/',views.prof,name='prof'),
    # url (r'^prof/',views.prof,ListView.as_view()),
    url(r'^newUser/',views.newUser,name="newUser"),
    url(r'^checkNew/',views.checknew,name="checkNew"),
     url(r'^checkRegister/',views.checkRegister,name="checkRegister"),
     url(r'^viewBusiness/',views.viewBusiness,name="viewBusiness"),
     url(r'^Members/',ListView.as_view(queryset=Member.objects.all(),template_name='x.html')),
     url(r'^editProf/',views.editProf,name='editProf'),
     url(r'^changePass/',views.changePass,name='changePass'),
     url(r'^pas/',views.pas,name='pas'),
    #url(r'^books/(\w+)/$', ABC.as_view()),
        ]