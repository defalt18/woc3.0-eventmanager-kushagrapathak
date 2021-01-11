from django.shortcuts import render
from EventMan.models import register,partregister,hosts
import uuid
from django.core.mail import send_mail
from datetime import date,timedelta
from twilio.rest import Client

# Create your views here.
def index(request):
    count= register.objects.all().count()
    count1= partregister.objects.all().count()
    data = register.objects.all()
    context = {'cnt': count,'pcnt':count1 , 'data' : data,}
    return render(request,'index.html',context)

def login(request):
    count= register.objects.all().count()
    count1= partregister.objects.all().count()
    context = {'cnt': count,'pcnt':count1 , 'status': '0',}
    return render(request,'login.html',context)

def showevent(request):
    if request.method=="POST" :
        name = request.POST.get('name')
        passw = request.POST.get('password')
        records = hosts.objects.filter(username=name,password=passw)
        context = {'status' : '-1'}
        if records.count()!=1 : 
            return render(request,'login.html',context)
        tp = register.objects.filter(email=name).values_list('name')
        events = register.objects.filter(email=name)
        tbs = []
        for i in range(tp.count()):
            tbs.append(str(tp[i])[2:len(str(tp[i]))-3])
        data = partregister.objects.filter(event_name__in=tbs)
        dtobs = {
            'eventdata' : events,
            'data' : data,
            'cnt': data.count(),
            'ecnt' : events.count(),
        }
        return render(request,'showevent.html',dtobs)

def home(request):
    count= register.objects.all().count()
    count1= partregister.objects.all().count()
    context = {'cnt': count,'pcnt':count1}
    return render(request,'home.html',context)

def ser(request):
    time = date.today() + timedelta(days=365)
    data = register.objects.filter(deadline__range= [date.today(),time])
    ref = {'data':data,'cnt':data.count(),'status':'0',}
    if request.method == 'POST' :
        p_id = str(uuid.uuid1())
        name = request.POST.get('name').title()
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        number = request.POST.get('pnum')
        event_name = request.POST.get('event_name')
        event_name = register.objects.filter(E_id = event_name).values('name')
        event_name = str(event_name[0])[10:len(str(event_name[0]))-2]
        if len(partregister.objects.filter(name= name,email=email,event_name=event_name)) == 0 :
            pregist = partregister(name = name,email=email,contact=contact,number=number,event_name=event_name,p_id=p_id)
            pregist.save()
            send_mail(f"Successfully registered for {event_name}", 
        f" {name} , You have been successfully registered for the event : {event_name} \n Your unique participant id is : {p_id} \n Total number of people: {number} \n\n Regards \n Event Manager App by Kushagra",
        "itschloe317@gmail.com",[str(email)],fail_silently=False)
            account_sid = 'sid'
            auth_token = 'token'
            client = Client(account_sid, auth_token)
            message = client.messages \
                            .create(
                                body=f"Thanks for registering with Event Manager \n Your details are : \n Name : {name} \n Unique Token ID : {p_id} \n Event Registered for : {event_name} \n Email : {email} \n \n \n Regards \n Event Manager App by Kushagra",
                                from_="xxxxxccc",
                                to=f"{contact}"
                            )
            return render(request,'part_page.html',{'data':data,'cnt':data.count(),'status':'1'})
        else : 
            return render(request,'part_page.html',{'data':data,'cnt':data.count(),'status':'-1'})

    return render(request,'part_page.html',ref)

def det(request):
    if request.method == 'POST' :
        E_id = str(uuid.uuid1())
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        deadline = request.POST.get('deadline')
        email = request.POST.get('email')
        link = request.POST.get('link')
        date = request.POST.get('date')
        password = request.POST.get('password')
        if hosts.objects.filter(username=email).count()==0 : 
            host_det = hosts(email = email,password=password,h_id=str(uuid.uuid1()),username=email)
            host_det.save()
        regist = register(name = name,email=email,desc=desc,deadline=deadline,link=link,date=date,E_id=E_id)
        regist.save()
        send_mail(f"Successfully registered : {name}", 
        f"You have successfully completed the event registration of the event : {name} \n Your Unique Event id is : {E_id} \n Event description : \n {desc} \n Deadline : {deadline} \n Link to the poster : {link} \n Event on : {date} \n \n\n Regards \n Event Manager App by Kushagra",
        "itschloe317@gmail.com",[str(email)],fail_silently=False)
    
    data = {
        'name':name,
        'desc':desc,
        'deadline':deadline,
        'email':email,
        'link':link,
        'date':date,
        'id' : E_id,
    }
    return render(request,'event.html',data)
