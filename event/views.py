from django.shortcuts import render
from django.db import models
from django.contrib.auth import models
from event.models import Event,Type,Subtype
from ticket.models import Ticket,Buy
from django.shortcuts import render, redirect
from account.models import User
from django.template import Context
from django.utils import dateparse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf


# Create your views here.


def eventDetailedView(request, event_id):

    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    myEvent = Event.objects.filter(id=event_id)
    username = models.User.objects.values_list('username')[0][0]
    newType = myEvent.values_list('type')[0][0]
    rate = myEvent.values_list('rate')[0][0]
    notrate = 5-rate
    myEvent = myEvent[0]

    if request.method == "POST":
        rate = request.POST.get("rate")
        print(rate)
        Event.objects.filter(id=event_id).update(rate=rate)
        rate = int(rate)

    return render(request, 'event.html', {'guest': not is_signed_in, 'signed_in': is_signed_in, 'admin': is_admin, 'type':newType, 'event': myEvent, 'rate': range(rate), 'notrange':range(notrate),'username':username})


def addType(request):
    if request.method == 'POST':
        type=request.POST.get("0")
        createtype = Type(type=type,name=type)
        t = Type.objects.filter(name=type);
        t2 = t.values_list('id')
        if len(t) < 1:
            createtype.save()
        else:
            types = Type.objects.get(id=t2)
            createtype = types
        for i in range(100):
            str1 = "input"+str(i)
            try:
                if not request.POST.get(str1) == "None":
                    subtype=Subtype(sub_type=request.POST.get(str1),name=request.POST.get(str1))
                    subtype.type = createtype
                    subtype.save()
            except :
                pass
    return redirect('/my-admin/types/all/')


def delType(request,typename):
    types = Type.objects.filter(name=typename)
    subtype = Subtype.objects.filter(type=types)
    subtype.delete()
    types.delete()

    return redirect('/my-admin/types/all/')


def delSubType(request,subtypename):

    subtype = Subtype.objects.filter(sub_type=subtypename)
    type = subtype.values_list('type')
    type = Type.objects.filter(id=type)[0]
    type=str(type)
    subtype.delete()
    str1 = '/my-admin/SubTypes/'+type

    return redirect(str1)


def edit_subtype(request,id):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    subtypename = Subtype.objects.filter(id=id).values_list('name')[0][0]
    if request.method == 'POST':
        str = request.POST.get("0")
        Subtype.objects.filter(id=id).update(sub_type=request.POST.get("0"),name=str)
        subtypename = Subtype.objects.filter(id=id).values_list('name')[0][0]
    return render(request,'edit-sub.html',{'id':id,'sub_type':subtypename,'guest': not is_signed_in, 'signed_in': is_signed_in, 'admin': is_admin,})


def eventsType(request, e_type):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    types1 = Type.objects.all()
    if e_type == 'all':
        allEvents = Event.objects.all()
        e_type = 'all'
        return render(request, 'events_admin.html', {'guest': not is_signed_in, 'signed_in': is_signed_in,
                                                     'admin': is_admin, 'types':types1, 'type': e_type,
                                                     'events': allEvents})
        # else:
        #     allEvents = Event.objects.filter(type=e_type)
        #     return render(request, 'subtypes.html', {'signed_in':True,'admin': True,'types':types1,'type': e_type, 'events': allEvents})


def ticketmanager(request,eventid):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    eventid1 = Event.objects.filter(id=eventid)
    eventname = eventid1.values_list('name')[0][0]
    tickets = Ticket.objects.filter(event=eventid)

    return render(request,'tickets.html', {'tickets':tickets,'name':eventname, 'id':eventid,
                                          'guest': not is_signed_in, 'signed_in': is_signed_in, 'admin': is_admin,})


def delete_tickets(request,ticketid):
    tick = Ticket.objects.filter(id=ticketid)
    eventid = tick.values_list('eventid')[0][0]
    current = Event.objects.filter(id=eventid).values_list('ticket_num')[0][0]
    current = current - 1;
    Ticket.objects.filter(id = ticketid).delete()
    Event.objects.filter(id=eventid).update(ticket_num=current)

    url = '/my-admin/tickets/'+str(eventid)
    return redirect(url)


def eventsSubtype(request, e_type, subtype):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    allEvents = Event.objects.filter(type=e_type)
    allEvents = allEvents.filter(sub_type=subtype)
    print(subtype)
    return render(request, 'events.html', {'guest': not is_signed_in, 'signed_in': is_signed_in, 'admin': is_admin, 'type': e_type, 'events': allEvents})


def subtypes (request, id):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    types = Type.objects.filter(id=id)
    typename = types.values_list('name')[0][0]
    subs1 = Subtype.objects.filter(type=types)
    allEvents = Event.objects.filter(type=types.values_list('name')[0][0])
    # allEvents = allEvents.filter(sub_type=sub)
    return render(request, 'subtypes.html', {'guest': not is_signed_in, 'signed_in': is_signed_in, 'admin': is_admin, 'type': typename, 'subtypes': subs1,'events':allEvents})


def subtype (request , id):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    sub1 = Subtype.objects.filter(id=id)
    allEvents = Event.objects.filter(sub_type=sub1.values_list('name')[0][0])
    mytype1 = sub1.values_list('type')
    mytype = Type.objects.filter(id=mytype1)
    mytype = mytype[0]
    return render(request, 'subtypes.html' , {'guest': not is_signed_in, 'signed_in': is_signed_in,
                                              'admin': is_admin, 'type':mytype,'subtypes': sub1,'events':allEvents})


def delete_events(request,event_id):
    Event.objects.filter(id=event_id).delete()
    return redirect('/my-admin/events/all/')
    # allEvents = Event.objects.all()
    # return render(request,'events.html',{'admin':True,'type':'all','events':allEvents})


def create_event(request,id):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    type1 = Type.objects.filter(id=id)
    typename=type1.values_list('name')[0][0]
    subs = Subtype.objects.filter(type=type1)
    if request.method == 'POST':
        name = request.POST['event_name']
        picture = request.POST['file-4[]']
        ticket_num = request.POST['event_ticket']
        desc = request.POST['info']
        date = request.POST['datepicker']
        deadline = request.POST['datepicker1']
        place = request.POST['event_place']
        type = type1.values_list('name')[0][0]
        sub_type = request.POST['genre']
        address = request.POST['event_addr']
        ticket_price = request.POST['event_price']
        duration = '2.0'
        event = Event(name=name,picture=picture,ticket_num=ticket_num,desc=desc,date=date,deadline=deadline,place=place,type=type,sub_type=sub_type,address=address,ticket_price=ticket_price,duration=duration, rate=0)
        event.save()
        for i in range(int(ticket_num)):
            ticket = Ticket(price=ticket_price,type='Normal',seat_num=i,event=event,buy=None,free=0)
            ticket.save();

    return render(request, 'event-adder.html',{'guest': not is_signed_in, 'signed_in': is_signed_in, 'admin': is_admin, 'id':id,'type':typename,'subtypes':subs})


def showsubs(request,typepid):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    type = Type.objects.filter(id=typepid)
    typename = type.values_list('name')[0][0]
    subtypes = Subtype.objects.filter(type=type)

    return render(request,'showsubtypes.html',{'subtypes':subtypes,'type':typename,'guest': not is_signed_in,
                                               'signed_in': is_signed_in, 'admin': is_admin})


def edit_event(request, event_id):
    is_signed_in = request.user.is_authenticated()
    is_admin = request.user.is_superuser
    if request.method=='POST':
        if not request.POST.get('event_name') == "":
            Event.objects.filter(id=event_id).update(name=request.POST.get('event_name'))
        if not request.POST.get('event_place') == "":
            Event.objects.filter(id=event_id).update(place=request.POST.get('event_place'))
        if not request.POST.get('file-4[]') == "":
            Event.objects.filter(id=event_id).update(picture=request.POST.get('file-4[]'))
        if not request.POST.get('event_ticket') == "":
            Event.objects.filter(id=event_id).update(ticket_num=request.POST.get('event_ticket'))
        if not request.POST.get('event_price') == "":
            Event.objects.filter(id=event_id).update(ticket_price=request.POST.get('event_price'))
        if not request.POST.get('datepicker') == "":
            Event.objects.filter(id=event_id).update(date=request.POST.get('datepicker'))
        if not request.POST.get('datepicker1') == "":
            Event.objects.filter(id=event_id).update(deadline=request.POST.get('datepicker1'))
        if not request.POST.get('event_addr') == "":
            Event.objects.filter(id=event_id).update(address=request.POST.get('event_addr'))
        if not request.POST.get('info') == "":
            Event.objects.filter(id=event_id).update(desc=request.POST.get('info'))

    event = Event.objects.filter(id=event_id)

    return render(request, 'virayesh.html', {'event': event[0], 'date':str(event[0].date),'deadline':str(event[0].deadline),'guest': not is_signed_in, 'signed_in': is_signed_in, 'admin': is_admin})
