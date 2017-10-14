from django.conf.urls import url
from adm import views
from django.views.generic import ListView,DetailView
from visiter.models import Member
urlpatterns=[
    url(r'(?P<pk>\d+)$',DetailView.as_view(model=Member,template_name="detailMem.html")),
    url(r'^$', views.Adminlogin, name="Adminlogin"),
     url(r'^Adminlogin/', views.Adminlogin, name="Adminlogin"),
     url(r'^ADcheck/', views.ADcheck, name="ADcheck"),
     url(r'^AdmincheckLogin/', views.AdmincheckLogin, name="AdmincheckLogin"),
     url(r'^logoutAdmin/', views.Adminlogout, name="Adminlogout"),
     url(r'^profileAdmin/', views.Adminprofile, name="Adminprofile"),
     url(r'^signup/', views.signup, name="signup"),
      url(r'^blank/', views.blank, name="blank"),
      url(r'^checkCate/',views.checkCate,name='checkCate'),
      url(r'^addCate/',views.addCate,name='addCate'),
       url(r'^memb/',ListView.as_view(queryset=Member.objects.all().order_by("name"),template_name='mem.html')),
    # url(r'^viewList/', views.viewList, name="signup"),
    # url(r'^addCate/', views.addCate, name="addCate"),
    #url(r'^$', views.Adminindex, name="Adminindex"),
     
     

    ]