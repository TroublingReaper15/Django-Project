from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,'home.html')

def home1(request,pk):
    data=Consumer.objects.get(id=pk)
    p=data.name
    q=data.email
    r=data.password
    z=data.id
    data={'p':p,'q':q,'r':r,'z':z}
    return render(request,'home.html',{'data':data})

def login(request):
    return render(request,'login.html')

def logout(request):
    return render(request,'home.html')

def registration(request):
    return render(request,'registration.html')

def register(request):
    user_name=request.POST.get('username')
    user_email=request.POST.get('email')
    user_phone=request.POST.get('phone')
    user_dob=request.POST.get('dob')
    user_gender=request.POST.get('gender')
    user_password=request.POST.get('password')
    user_cpassword=request.POST.get('cpassword')
    user=Consumer.objects.filter(email = user_email)
    if user:
        msg="User/Email already exist !!!"
        return render(request,'registration.html',{'msg':msg})
    else:
        if (user_password == user_cpassword):
            user_data=Consumer.objects.create(name=user_name,email=user_email,contact=user_phone,dob=user_dob,gender=user_gender,password=user_password)
            msg="User Registration Successful"
            return render(request,'login.html',{'msg':msg})
        else:
            msg="Pass & Cpass not match !!!"
            return render(request,'registration.html',{'msg':msg})

def dash(request,pk):
    data=Consumer.objects.get(id=pk)
    p=data.name
    q=data.email
    r=data.password
    z=data.id
    a=data.contact
    b=data.dob
    c=data.gender
    data={'p':p,'q':q,'r':r,'z':z,'a':a,'b':b,'c':c}
    return render(request,'dash.html',{'data':data})

def query(request,pk):
    data=Consumer.objects.get(id=pk)
    p=data.name
    q=data.email
    r=data.password
    z=data.id
    data={'p':p,'q':q,'r':r,'z':z}
    return render(request,'query.html',{'data':data})

def dashboard(request):
    user_email=request.POST.get('loginemail')
    user_password=request.POST.get('loginpassword')
    user=Consumer.objects.filter(email=user_email)
    if user:
        data=Consumer.objects.get(email=user_email)
        p=data.name
        q=data.email
        r=data.password
        z=data.id
        data={'p':p,'q':q,'r':r,'z':z}
        if user_password==r:
            if user_password==r:
                if user_email=='admin@gmail.com':
                    data=Consumer.objects.get(email='admin@gmail.com')
                    email=data.email
                    name=data.name
                    id=data.id
                    dob=data.dob
                    contact=data.contact
                    gender=data.gender
                    password=data.password
                    admindata={'name':name,"email":email,"contact":contact,"gender":gender,"password":password,"dob":dob}
                    return render(request,'dash.html',{'admindata':admindata})
                else:
                    return render(request,'home.html',{'data':data})
        else:
            msg="Password not matched !!!"
            return render(request,'login.html',{'msg':msg})
    else:
        msg="Email not register !!!"
        return render(request,'registration.html',{'msg':msg})

def querydata(request,pk):
    name = request.POST.get('name')
    email = request.POST.get('email')
    query = request.POST.get('query')
    Query.objects.create(name=name,email=email,query=query)
    data=Consumer.objects.get(id=pk)
    p=data.name
    q=data.email
    z=data.id
    data={'p':p,'q':q,'z':z}
    return render (request,'query.html',{'data':data,'data1':data})

def data(request,pk):
    data=Consumer.objects.get(id=pk)
    p=data.name
    q=data.email
    r=data.password
    z=data.id
    querydata = Query.objects.filter(email=q)
    data={'p':p,'q':q,'r':r,'z':z}
    return render(request,'querydata.html',{'data':data,'data2':querydata})

def delete(request,pk):
    data=Query.objects.get(id=pk)
    email=data.email
    data.delete()
    querydata = Query.objects.filter(email=email)
    data=Consumer.objects.get(email=email)
    p=data.name
    q=data.email
    z=data.id
    data={'p':p,'q':q,'z':z}
    return render (request,'querydata.html',{'data':data,'data1':data,'data2':querydata})

def edit(request,pk):
    # print(pk)
    data=Query.objects.get(id=pk)
    name=data.name
    email=data.email
    id=data.id
    query=data.query
    dataquery={'n':name,'e':email,'id':id,'query':query}
    querydata = Query.objects.filter(email=email)
    data=Consumer.objects.get(email=email)
    p=data.name
    q=data.email
    z=data.id
    data={'p':p,'q':q,'z':z}
    return render (request,'query.html',{'data':data,'data3':dataquery,'data2':querydata})

def search(request,pk):
        search_query=request.POST.get('searching')
        all_data1=Query.objects.filter( Q(name__icontains=search_query) |Q(email__icontains=search_query) | Q(query__icontains=search_query))
        data=Consumer.objects.get(id=pk)
        p=data.name
        q=data.email
        z=data.id
        data={'p':p,'q':q,'z':z}
        all_data=all_data1.filter(email=q)
        return render(request,'querydata.html',{'data':data,'queryshow':all_data})

def update(request,pk):
    query = request.POST.get('query')
    data1=Query.objects.get(id=pk)
    data1.query=query
    email=data1.email
    data1.save()
    querydata = Query.objects.filter(email=email)
    data=Consumer.objects.get(email=email)
    p=data.name
    q=data.email
    z=data.id
    data={'p':p,'q':q,'z':z}
    return render (request,'querydata.html',{'data':data,'data2':querydata})

def admin_data(request):
    data=Consumer.objects.get(email='admin@gmail.com')
    name=data.name
    email=data.email
    id=data.id
    dob=data.dob
    contact=data.contact
    gender=data.gender
    password=data.password
    admindata={'name':name,"email":email,"contact":contact,"gender":gender,"password":password,"dob":dob}
    return render(request,'dash.html',{'admindata':admindata})

def admin_email(request):
    data=Consumer.objects.get(email='admin@gmail.com')
    name=data.name
    email=data.email
    id=data.id
    dob=data.dob
    contact=data.contact
    gender=data.gender
    password=data.password
    admindata={'name':name,"email":email,"contact":contact,"gender":gender,"password":password,"dob":dob}
    data=Consumer.objects.values()
    return render(request,'email.html',{'admindata':admindata,'alldata':data})

def admin_query(request):
    data=Consumer.objects.get(email='admin@gmail.com')
    name=data.name
    email=data.email
    id=data.id
    dob=data.dob
    contact=data.contact
    gender=data.gender
    password=data.password
    admindata={'name':name,"email":email,"contact":contact,"gender":gender,"password":password,"dob":dob}
    data=Query.objects.values()
    return render(request,'querydata1.html',{'admindata':admindata,'alldata':data})