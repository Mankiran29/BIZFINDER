from django.http.response import HttpResponse
from django.template import loader
from django.shortcuts import render
from adm.models import ADMember,Categories
from visiter.models import Member,Registration
from django.http import Http404
def checkCate(request):
    m=Categories()
    Aname=request.POST['category']
    m.cate=Aname
    m.save()
    return render(request,'cate.html',{'msg':'done'})
def addCate(request):
    return render(request,'cate.html')
    
    
    
def signup(request):
    return HttpResponse(loader.get_template('sign.html').render())
def Adminindex(request):
    return render(request, 'admBase.html')
def blank(request):
    m=Registration.objects.all()
    return render(request,'blank.html',{'m':m})
def AdmincheckLogin(request):
    if request.method!='POST':
        raise Http404('Only POSTs are allowed')
    
    try:
        m=ADMember.objects.get(emailM=request.POST['nametext'])
        if m.password == request.POST['passwordtext']:
            request.session["UserSession"]=m.name
            request.session.modified=True
            a=Member.objects.count()
            b=Registration.objects.count()
            c=Categories.objects.count()
            d=Registration.objects.filter(status='pending').count()
            response=render(request, 'admBase.html',{'user':m.name,'a':a,'b':b,'c':c,'d':d})
            if 'check' in request.POST:
                response.set_cookie(key="name",value="userName",max_age=10*60*60)
            return response
        
    except ADMember.DoesNotExist:
        return render(request,'loginAdm2.html',{'msg':"Invalid"})#    else:
    return render(request,'loginAdm2.html')
def ADcheck(request):
    m=ADMember()
    Aname=request.POST['name']
    Aemail=request.POST['nametext']
    Apassword=request.POST['passwordtext']
    passwordcon=request.POST["passwordtextA"]
    if(Apassword == passwordcon):
        m.name=Aname
        m.emailM=Aemail
        m.password=Apassword
        m.save()
        return render(request,'loginAdm2.html')
    else:
        return render(request,'sign.html',{'msg':'Invalid'}) 
def Adminlogin(request):
    if "UserName" in request.COOKIES:
        cooki=request.COOKIES["UserName"]
        request.session["UserSession"]=cooki
        request.session.modified=True
        return render(request, 'BaseAdm.html', {'user':request.session["UserSession"], 'pass':""})
    return render(request, 'loginAdm2.html')
def Adminlogout(request):
    del request.session["UserSession"]
    response=render(request, 'loginAdm.html')
    response.set_cookie(key="UserName", value="", max_age=0)
    return response
def Adminprofile(request):
    return render(request,'profileAdm.html')