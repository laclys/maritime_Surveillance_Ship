from django.shortcuts import render_to_response

from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from models import User2,Ship

# Create your views here.
class UserForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'on','placeholder':'Type name',}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password',}))
    cpassword=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password',}))
    number=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Number',}))
    position=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Position',}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'E-mail',}))
    firstname=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name',}))
    lastname=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Nmae',}))
    phone=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Phone Number',}))
    address=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Address',}))



class UserForm2(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'on','placeholder':'Type name',}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password',}))
    

class Modification1(forms.Form):
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'E-mail',}))


class Modification2(forms.Form):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password',}))    
class Modification3(forms.Form):
    phone=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Phone Number',}))
class Modification4(forms.Form):
    address=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Address',}))

def regist(req):
    if req.method =='POST':
        uf=UserForm(req.POST)
        if uf.is_valid():
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']
            cpassword=uf.cleaned_data['cpassword']
            number=uf.cleaned_data['number']
            position=uf.cleaned_data['position']
            email=uf.cleaned_data['email']
            firstname=uf.cleaned_data['firstname']
            lastname=uf.cleaned_data['lastname']
            phone=uf.cleaned_data['phone']
            address=uf.cleaned_data['address']
            if password==cpassword:
                print username,password,cpassword,number,position,email,firstname,lastname,phone,address
                User2.objects.create(username=username,password=password,number=number,position=position,email=email,firstname=firstname,lastname=lastname,phone=phone,address=address)
                #zyy=User2()
                #zyy.username=username
                #zyy.password=password
                #zyy.save()
                return HttpResponseRedirect('/login/')
            else:
                uf=UserForm()
    
    else:
        uf=UserForm()
    return render_to_response('regi.html',{'uf':uf})



def login(req):
    if req.method =='POST':
        uf=UserForm2(req.POST)
        if uf.is_valid():
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']
            print username,password
            users=User2.objects.filter(username=username,password=password)
            if users:
                req.session['username']=username
                response= HttpResponseRedirect('/index/')
                #response.set_cookie('username',username,3600)
                return response
            else:
                return HttpResponseRedirect('/login/')
    
    else:
        uf=UserForm()
    return render_to_response('login.html',{'uf':uf})


def index(req):
    #username=req.COOKIES['username']
    ##username=req.COOKIES.get('username','')
    #return HttpResponse('nice boy %s' % username)
    username=req.session.get('username',)
    ships = Ship.objects.all()
    return render_to_response('index.html',{'username':username,'ships':ships})


def logout(req):
    
    #response=HttpResponse('logout')
    #response.delete_cookie('username')
    #return response
    del req.session['username']
    
    return render_to_response('logout.html')


def center(req):
    username=req.session.get('username',)
    try:
        person = User2.objects.get(username=username)
        uf=Modification1(req.POST)
        if uf.is_valid():
            email=uf.cleaned_data['email']
            person.email=email
            person.save()
        ut=Modification2(req.POST)
        if ut.is_valid():
            password=ut.cleaned_data['password']
            person.password=password
            person.save()
        ua=Modification3(req.POST)
        if ua.is_valid():
            phone=ua.cleaned_data['phone']
            person.phone=phone
            person.save()
        ub=Modification4(req.POST)
        if ub.is_valid():
            address=ub.cleaned_data['address']
            person.address=address
            person.save()
        ##person = User2.objects.all()
        return render_to_response("person.html",{'username':username,'person':person,'uf':uf,'ut':ut,'ua':ua,'ub':ub})
    except User2.DoesNotExist:
        return render_to_response("person.html",)
