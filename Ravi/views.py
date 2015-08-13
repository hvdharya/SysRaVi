from django.shortcuts import render, render_to_response
from account.models import User
from django.contrib.auth import models
from event.models import Event,Type
from ticket.models import Buy,Ticket


def mainPage(request):
    myevent = Event.objects.order_by('-rate')
    newest = Event.objects.order_by('-date')
    types = Type.objects.all()
    new_event = []
    best_events = []
    index1 = min(len(newest),5)
    for i in range(index1):
        new_event.append(newest[i])
    index = min(len(myevent),5)
    for i in range(index):
        best_events.append(myevent[i])

    return render(request, 'main.html', {'signed_in': True,'admin':False, 'best_events': best_events,'newest_event':new_event,'types':types})


def startPage(request):

    return render(request, 'start.html', {'signed_in': True})


def user(request):
    return render(request, 'userProfile.html', {'signed_in': True})


def modir(request):

    types = Type.objects.all()
    return render(request, 'my-admin.html', {'signed_in': True, 'admin': True,'types':types})


def add(request):
    return render(request, 'events_admin.html')


def signup(request):
    return  render(request,'sign-up.html',{'signed_in':True})


def adminSetting(request):

    superUser = 'hvdh'
    djangoUser = models.User.objects.filter(username=superUser)
    myUser = User.objects.filter(user = djangoUser)
    address = myUser.values_list('address',flat=True)
    gender = myUser.values_list('gender',flat=True)
    tel = myUser.values_list('phone_num',flat=True)
    mail = djangoUser.values_list('email',flat=True)
    pic = myUser.values_list('avatar',flat=True)
    name = djangoUser.values_list('first_name',flat=True)
    lastname = djangoUser.values_list('last_name',flat=True)

    if request.method == 'POST':
        if not request.POST.get('tel') == "":
            User.objects.filter(user=djangoUser).update(phone_num=request.POST.get('tel'))
        if not request.POST.get('addr') == "":
            User.objects.filter(user=djangoUser).update(address=request.POST.get('addr'))
        if not request.POST.get('file-4[]') == "":
            User.objects.filter(user=djangoUser).update(avatar=request.POST.get('file-4[]'))
        if not request.POST.get('name') == "":
            models.User.objects.filter(username=superUser).update(first_name=request.POST.get('name'))
        if not request.POST.get('lastname') == "":
            models.User.objects.filter(username=superUser).update(last_name=request.POST.get('lastname'))
        if not request.POST.get('mail') == "":
            models.User.objects.filter(username=superUser).update(email=request.POST.get('mail'))


    return render(request, 'admin.html',
                  {'picture': pic, 'username':superUser, 'lastname':lastname, 'tel':tel, 'name':name, 'addr':address, 'mail':mail[0],'signed_in':True,'admin':True}
                  )


def edit_see(request, username):

    djangoUser = models.User.objects.filter(id=username)
    usern = djangoUser.values_list('username')[0]
    myUser = User.objects.filter(user = djangoUser)
    buys = Buy.objects.filter(user=myUser)
    buyid = buys.values_list('id')
    if len(buys) != 0:
        for i in range(len(buyid)):
            event=(Ticket.objects.filter(buy=buys[i])).values_list('event')
        for i in range(len(event)):
            names = event[i]
    address = myUser.values_list('address',flat=True)
    gender = myUser.values_list('gender',flat=True)
    tel = myUser.values_list('phone_num',flat=True)
    mail = djangoUser.values_list('email',flat=True)
    pic = myUser.values_list('avatar',flat=True)
    name = djangoUser.values_list('first_name',flat=True)
    lastname = djangoUser.values_list('last_name',flat=True)

    if request.method == 'POST':
        if not request.POST.get('tel') == "":
            User.objects.filter(user=djangoUser).update(phone_num=request.POST.get('tel'))
        if not request.POST.get('addr') == "":
            User.objects.filter(user=djangoUser).update(address=request.POST.get('addr'))
        if not request.POST.get('file-4[]') == "":
            User.objects.filter(user=djangoUser).update(avatar=request.POST.get('file-4[]'))
        if not request.POST.get('name') == "":
            models.User.objects.filter(username=username).update(first_name=request.POST.get('name'))
        if not request.POST.get('lastname') == "":
            models.User.objects.filter(username=username).update(last_name=request.POST.get('lastname'))
        if not request.POST.get('mail') == "":
            models.User.objects.filter(username=username).update(email=request.POST.get('mail'))

    return render(request, 'profile_edit.html',
                  {'buys':buys,'img_address': pic[0], 'username':usern[0], 'lastname':lastname[0], 'tel':tel[0], 'name':name[0], 'addr':address[0], 'mail':mail[0],'signed_in': True}
                  )

