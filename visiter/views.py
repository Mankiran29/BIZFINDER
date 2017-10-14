from django.http.response import HttpResponse
from django.template import loader
from django.shortcuts import render, render_to_response
from visiter.models import Member,Registration
from django.http import Http404
from adm.models import Categories
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
#class Display(ListView):
#    template_name='prof.html'
#    queryset=Member.objects.get()
#    model=Member
#class ABC(ListView):

 #   context_object_name = "book_list"
 #   template_name = "prof.html"

  #  def get_queryset(self):
  #      publisher = get_object_or_404(Member, name__iexact=self.args[0])
  #      return Member.objects.filter(publisher=publisher)
#class UserprojectList(ListView):
#    context_object_name = 'userproject_list'
#    template_name = 'prof.html'
#    def get_queryset(self):
#        return Member.objects.filter(name=self.request.user)
#class memberDetail(ListView):
#    template_name=prof.html
#    queryset=Member.objects.all().filter(name = request.session["UserSession"])
def editProf(request):
    m=Member.objects.get(name = request.session["UserSession"])
    m.firstName=request.POST['firstName']
    m.lastName=request.POST['lastName']
    m.emailM=request.POST['email']
    m.phoneM=request.POST['phone']
    m.addressM=request.POST['address']
    m.save()
    msg="Changes Done!"
    return render(request,'prof.html',{'msg':msg})
def prof(request): 
    m = Member.objects.all().filter(name = request.session["UserSession"])
    #abc={'name':m[0].name}
   # name = request.session["UserSession"]
   # abc = Member.objects.values_list(
   #     'name', flat=True
   # ).distinct()
   # x=Member.__iter__()
    return render_to_response('prof.html',{"m":m[0]})
def changePass(request):
    m=Member.objects.get(name = request.session["UserSession"])
    pas1=request.POST['passw1']
    pas2=request.POST["passw2"]
    if(pas1 == pas2):
        m.password=pas1
        m.save()
        return render(request,'prof.html',{'msg':"Changes done!"})
    else:
        return render(request,'changePass.html',{'msg':'Invalid'})   
    
def pas(request):
    return render(request,'changePass.html')    
    
def index(request):
    return render(request, 'index.html')
def about(request):
    return HttpResponse(loader.get_template('index.html').render())
def contact(request):
    return HttpResponse(loader.get_template('index.html').render())
def login(request):
    if "UserName" in request.COOKIES:
        cooki=request.COOKIES["UserName"]
        request.session["UserSession"]=cooki
        request.session.modified=True
        return render(request, 'profile.html', {'user':request.session["UserSession"], 'pass':""})
    return render(request, 'generic.html')
def logout(request):
    del request.session["UserSession"]
    response=render(request, 'generic.html')
    response.set_cookie(key="UserName", value="", max_age=0)
    return response
def viewBusiness(request):
    response=render(request, 'generic.html')
    return response
def checknew(request):
    m=Member()
    Aname=request.POST['nameText']
    Apassword=request.POST['passwordText']
    passwordcon=request.POST["confirmPassword"]
    if(Apassword == passwordcon):
        m.name=Aname
        m.password=Apassword
        m.firstName=request.POST['firstName']
        m.lastName=request.POST['lastName']
        m.emailM=request.POST['email']
        m.phoneM=request.POST['phone']
        m.addressM=request.POST['address']
        m.save()
        return render(request,'generic.html')
    else:
        return render(request,'newUser.html',{'msg':'Invalid'})      
def newUser(request):
    return render(request,'newUser.html') 
def checkRegister(request): 
    m=Member.objects.get(name = request.session["UserSession"])
    if(request.POST['name']):
        r=Registration()
        r.name=request.POST['name']
        r.prName=request.POST['prName']
        r.email=request.POST['email']
        r.phone=request.POST['phone']
        r.address=request.POST['address']
        r.city=request.POST['city']
        r.category=request.POST['category']
        r.status='pending'
        r.save()
        return render(request,'profile.html')
    else:
        return render(request,'newUser.html',{'msg':'Invalid'})  
    
def business(request):
    name = request.session["UserSession"]
    r=Registration.objects.get(name = request.session["UserSession"])  
    #print(r.prName)
    print(name)
    return render(request,'profile.html',{'r':r})
    
    
def register(request):
    return HttpResponse(loader.get_template('register.html').render())
def checkLogin(request):
    if request.method!='POST':
        raise Http404('Only POSTs are allowed')
    try:
        m=Member.objects.get(name=request.POST['nameText'])
        if m.password == request.POST['passwordText']:
            request.session["UserSession"]=m.name
            request.session.modified=True
            response=render(request, 'profile.html',{'user':m.name,'pass':''})
            if 'check' in request.POST:
                response.set_cookie(key="name",value="userName",max_age=10*60*60)
            return response
    except Member.DoesNotExist:
        return render(request,'generic.html',{'msg':"Invalid"})#    else:
    return render(request,'generic.html')
    
##    if 'nameText' in request.POST:
##       password=request.POST["passwordText"]
#      if(userName=="noor" and password=="29"):
#           request.session["UserSession"]=userName
#           request.session.modified=True
##            #if 'check' in request.POST:
#               #response.set_cookie(key="UserName",value="noor",max_age=10*60*60)
#            return response
#       else:
#           return render(request,'generic.html',{'msg':"Invalid"})
#    else:
#        return render(request,'generic.html')
def prof1(request): 
    m=Member.objects.filter(name=request.session["UserSession"])
    print(m[0])
    return render_to_response('prof.html',{'m':m})
        
def addBus(request):
    if 'UserSession' in request.session:
        m = Member.objects.all().filter(name = request.session["UserSession"]).first()
        a=Categories.objects.all
        n=m.name
        return render(request,'register.html',{'a':a,'n':n})
    else:
        return render(request,'generic.html')

        
def category(request):
    print()
    
