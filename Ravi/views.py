from django.shortcuts import render, render_to_response,redirect
from account.models import User
from django.contrib.auth import models
from event.models import Event,Type
from ticket.models import Buy,Ticket


def mainPage(request):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
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

    return render(request, 'main.html', {'signed_in': is_signed_in,'admin':is_admin, 'guest': not is_signed_in, 'best_events': best_events,'newest_event':new_event,'types':types})


def startPage(request):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    return render(request, 'start.html', {'signed_in': is_signed_in,'admin':is_admin, 'guest': not is_signed_in})


def user(request):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    return render(request, 'userProfile.html', {'signed_in': is_signed_in,'admin':is_admin, 'guest': not is_signed_in})


def modir(request):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    types = Type.objects.all()
    return render(request, 'my-admin.html', {'signed_in': is_signed_in,'admin':is_admin, 'guest': not is_signed_in,'types':types})


def add(request):
    return render(request, 'events_admin.html')


def signup(request):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    return  render(request,'sign-up.html',{'signed_in': is_signed_in,'admin':is_admin, 'guest': not is_signed_in})


def adminSetting(request):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
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
                  {'picture': pic, 'username':superUser, 'lastname':lastname,
                   'tel':tel, 'name':name, 'addr':address, 'mail':mail[0],
                   'signed_in': is_signed_in,'admin':is_admin, 'guest': not is_signed_in}
                  )

def profile(request):

    id = request.user.id
    if id != 1:
        djangoUser = models.User.objects.filter(id=id)
        usern = User.objects.filter(user=djangoUser)
        if usern.values_list('userType')[0][0] == "owner":
            events = Event.objects.filter(owner=usern)
            types = Type.objects.all()
            return render(request,'owner.html',{'id':id,'types':types,'events':events})
        else:
            return edit_see(request,id)
    else:
        return redirect('')


def edit_see(request,id):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    djangoUser = models.User.objects.filter(id=id)
    usern = djangoUser.values_list('username')[0]
    myUser = User.objects.filter(user = djangoUser)
    buys = Buy.objects.filter(user=myUser)
    buyid = buys.values_list('id')
    if len(buys) != 0:
        for i in range(len(buyid)):
            event=(Ticket.objects.filter(buy=buys[i])).values_list('event')
        for i in range(len(event)):
            names = event[i]
    types1 = Type.objects.all()
    address = myUser.values_list('address',flat=True)
    gender = myUser.values_list('gender',flat=True)
    tel = myUser.values_list('phone_num',flat=True)
    mail = djangoUser.values_list('email',flat=True)
    pic = myUser.values_list('avatar',flat=True)
    name = djangoUser.values_list('first_name',flat=True)
    lastname = djangoUser.values_list('last_name',flat=True)
    usertype = myUser.values_list('userType')
    if request.method == 'POST':
        if not request.POST.get('tel') == "":
            User.objects.filter(user=djangoUser).update(phone_num=request.POST.get('tel'))
        if not request.POST.get('addr') == "":
            User.objects.filter(user=djangoUser).update(address=request.POST.get('addr'))
        if not request.POST.get('file-4[]') == "":
            User.objects.filter(user=djangoUser).update(avatar=request.POST.get('file-4[]'))
        if not request.POST.get('name') == "":
            models.User.objects.filter(username=usern).update(first_name=request.POST.get('name'))
        if not request.POST.get('lastname') == "":
            models.User.objects.filter(username=usern).update(last_name=request.POST.get('lastname'))
        if not request.POST.get('mail') == "":
            models.User.objects.filter(username=usern).update(email=request.POST.get('mail'))
        if not request.POST.get('usertype') == "":
            User.objects.filter(user=djangoUser).update(userType=request.POST.get('usertype'))
    return render(request, 'profile_edit.html',
                  {'buys':buys,'img_address': pic[0], 'username':usern[0], 'lastname':lastname[0],
                   'tel':tel[0], 'name':name[0], 'addr':address[0], 'mail':mail[0],'signed_in': is_signed_in,
                   'admin':is_admin, 'guest': not is_signed_in,'usertype':usertype[0][0]}
                  )

