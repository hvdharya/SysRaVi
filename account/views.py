from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.db import models
from account.models import User
from django.contrib.auth import models,authenticate,login, logout
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from event.models import Event,Type,Subtype
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.


@user_passes_test(lambda u: u.is_active and u.is_superuser)
def allUsers(request):
    user = models.User.objects.all()
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    return render(request, 'users.html', {'signed_in': is_signed_in, 'admin': is_admin, 'guest': not is_signed_in, 'users': user})


@user_passes_test(lambda u: u.is_active and u.is_superuser)
def delUsers(request,userid):
    myUser=models.User.objects.filter(id=userid)
    user = User.objects.filter(user=myUser)
    user.delete()
    myUser.delete()
    return redirect('/my-admin/users/all/')


def create_account(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        djuser = models.User.objects.create_user(username = request.POST['usr'],
                                                 email = request.POST['mail'],
                                                 password= request.POST['pass'],
                                                 )
        djuser.first_name = request.POST['name'],
        djuser.last_name = request.POST['lastname'],
        user = User( address = request.POST['addr'],
                     phone_num = request.POST['tel'],
                     gender = request.POST['gender'],
                     avatar = request.POST['file-4[]'],
                     userType = 'Normal',
                     )
        user.user = djuser
        djuser.save()
        user.save()
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    return render(request,"main.html",{'signed_in': is_signed_in, 'admin': is_admin, 'guest': not is_signed_in})


def login_to_site(request):

    username = request.POST.get("username")
    password = request.POST.get("password")
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            if request.user.is_superuser:
                return redirect('/my-admin/')
                # return render(request, 'admin.html', {'signed_in': True})
            else:
                signed_in = True
                return redirect('/main/')
        else:
            deactivated = True
    else:
        return HttpResponse("not registerd")


@login_required(redirect_field_name='/', login_url='/')
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')


def events(request, e_type):

    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    types1 = Type.objects.all()
    # subtype1 = Subtype.objects.filter(type=type2)
    if e_type == 'all':
        allEvents = Event.objects.all()
        e_type = 'all'
        return render(request, 'events.html', {'signed_in': is_signed_in,'admin': is_admin, 'guest': not is_signed_in, 'types':types1, 'type': e_type, 'events': allEvents})
    else:
        allEvents = Event.objects.filter(type=e_type)
        return render(request, 'events.html', {'signed_in': is_signed_in,'admin': is_admin, 'guest': not is_signed_in, 'type': e_type, 'events': allEvents})


def eventsSub(request, e_type, subtype):

    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    allEvents = Event.objects.filter(type=e_type)
    allEvents = allEvents.filter(sub_type=subtype)
    return render(request, 'events.html', {'signed_in': is_signed_in,'admin': is_admin, 'guest': not is_signed_in, 'type': e_type, 'events': allEvents})


def eventsall(request):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    allEvents = Event.objects.all()
    types1 = Type.objects.all()
    return render(request, 'events.html', {'signed_in': is_signed_in,'admin': is_admin, 'guest': not is_signed_in,'types':types1, 'type':'all', 'events': allEvents})


@user_passes_test(lambda u: u.is_active and u.is_superuser)
def types(request):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    alltypes = Type.objects.all()
    return render(request, 'types.html', {'types':alltypes, 'signed_in': is_signed_in, 'admin': is_admin, 'guest': not is_signed_in})


@login_required(redirect_field_name='/', login_url='/')
def portal(request,eventid):
    userid = request.user.id
    price = Event.objects.filter(id=eventid).values_list('ticket_price')
    if request.method == 'POST':
        total = request.POST.get("ticket_num")
        number = total
        total = (int(total))*(int(price[0][0]))

    return render(request,'buy.html',{'total':total,'userid':userid,'eventid':eventid,'ticket_num':number})

