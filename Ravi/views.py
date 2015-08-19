from django.shortcuts import render, render_to_response,redirect
from account.models import User
from django.contrib.auth import models
from event.models import Event,Type
from ticket.models import Buy, Ticket
from django.contrib.auth.decorators import user_passes_test, login_required
import datetime


def mainPage(request):


    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d")
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    events = Event.objects.filter(deadline__gte=now)
    myevent = events.order_by('-rate')
    newest = events.order_by('-date')
    types = Type.objects.all()
    new_event = []
    best_events = []
    index1 = min(len(newest),5)
    for i in range(index1):
        new_event.append(newest[i])
    index = min(len(myevent),5)
    for i in range(index):
        best_events.append(myevent[i])
    if request.user.is_anonymous():
        return render(request, 'main.html', {'signed_in': is_signed_in,'admin':is_admin, 'guest': not is_signed_in, 'best_events': best_events,'newest_event':new_event,'types':types,'username':'Guest'})
    else:
        return render(request, 'main.html', {'signed_in': is_signed_in,'admin':is_admin, 'guest': not is_signed_in, 'best_events': best_events,'newest_event':new_event,'types':types,'username':(request.user.first_name[2:-3])})


def startPage(request):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    return render(request, 'start.html', {'signed_in': is_signed_in,'admin':is_admin, 'guest': not is_signed_in})


@login_required(redirect_field_name='/', login_url='/')
def user(request,id):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    return render(request, 'userProfile.html', {'signed_in': is_signed_in,'admin':is_admin, 'guest': not is_signed_in})


@user_passes_test(lambda u: u.is_active and u.is_superuser)
def modir(request):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    types = Type.objects.all()
    return render(request, 'my-admin.html', {'signed_in': is_signed_in,'admin':is_admin, 'guest': not is_signed_in,'types':types})


def signup(request):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    return render(request,'sign-up.html',{'signed_in': is_signed_in,'admin':is_admin, 'guest': not is_signed_in})


@user_passes_test(lambda u: u.is_active and u.is_superuser)
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


@login_required(redirect_field_name='/', login_url='/')
def profile(request):

    owner = False
    id = request.user.id
    events=None
    if id != 1:
        djangoUser = models.User.objects.filter(id=id)
        usern = User.objects.filter(user=djangoUser)
        if usern.values_list('userType')[0][0] == "owner":
            events = Event.objects.filter(owner=usern)
            owner = True
    types = Type.objects.all()
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
                  {'buys':buys,'img_address': pic[0], 'username':usern[0], 'lastname':lastname[0][2:-3],
                   'tel':tel[0], 'name':name[0][2:-3], 'addr':address[0], 'mail':mail[0],'signed_in': is_signed_in,
                   'admin':is_admin, 'guest': not is_signed_in,'usertype':usertype[0][0],'owner':owner,'types':types,'events':events}
                  )

@login_required(redirect_field_name='/', login_url='/')
def profile_settings(request):

    id = request.user.id
    return edit_see(request,id)


@login_required(redirect_field_name='/', login_url='/')
def edit_see(request,id):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    djangoUser = models.User.objects.filter(id=id)
    usern = djangoUser.values_list('username')[0]
    myUser = User.objects.filter(user = djangoUser)
    buys = Buy.objects.filter(user=myUser)
    buyid = buys.values_list('id')
    events=None
    if len(buys) != 0:
        for i in range(len(buyid)):
            event=(Ticket.objects.filter(buy=buys[i])).values_list('event')
        for i in range(len(event)):
            names = event[i]
    types1 = Type.objects.all()
    owner=False;
    address = myUser.values_list('address',flat=True)
    gender = myUser.values_list('gender',flat=True)
    tel = myUser.values_list('phone_num',flat=True)
    mail = djangoUser.values_list('email',flat=True)
    pic = myUser.values_list('avatar',flat=True)
    name = djangoUser.values_list('first_name',flat=True)
    lastname = djangoUser.values_list('last_name',flat=True)
    usertype = myUser.values_list('userType')
    if usertype[0][0]=='owner':
        owner = True
        events = Event.objects.filter(owner=myUser)
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
            if usertype[0][0]=='owner':
                owner = True
                events = Event.objects.filter(owner=myUser)
            else:
                owner = False
    return render(request, 'profile_edit.html',
                  {'buys':buys,'img_address': pic[0], 'username':usern[0], 'lastname':lastname[0][2:-3],
                   'tel':tel[0], 'name':name[0][2:-3], 'addr':address[0], 'mail':mail[0],'signed_in': is_signed_in,
                   'admin':is_admin, 'guest': not is_signed_in,'usertype':usertype[0][0],'owner':owner,'events':events}
                  )


def search_event(request):
    search1 = request.POST.get("search")
    print(search1)
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    pattern= r"\b%s\b" %search1
    # print(pattern)
    events  = Event.objects.filter(name__regex=search1)
    print(events)

    return render(request,'Search.html',{'events':events,'signed_in':is_signed_in,'admin':is_admin,'guest':not is_signed_in})
