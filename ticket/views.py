from django.shortcuts import render, redirect
from ticket.models import Buy,Ticket,Cart
from event.models import Event
from account.models import User
from django.db import models
from django.contrib.auth import models
from django.contrib.auth.decorators import user_passes_test, login_required
# Create your views here.


@login_required(redirect_field_name='/', login_url='/')
def buy(request,userid,eventid):
    price = Event.objects.filter(id=eventid).values_list('ticket_price')[0][0]
    purchasecode = str(userid)+str(eventid)+'396'
    purchasecode = int(purchasecode)

    if request.method == 'POST':
        numberoftickets = request.POST.get("ticket_num")
        traceid = str(userid)+str(eventid)+str(numberoftickets)+str(128)+str(price)
        traceid = int(traceid)
        myUser=models.User.objects.filter(id=userid)
        user = User.objects.get(user=myUser)
        event = Event.objects.get(id=eventid)
        avail = event.available_tickets
        if int(numberoftickets) >= avail:
            numberoftickets = avail
        else:
            avail = avail - int(numberoftickets)
        Event.objects.filter(id=eventid).update(available_tickets=avail)
        mytick = Ticket.objects.filter(event=event,free=0)
        availticks = mytick.values_list('id')
    try:
        for i in range(int(numberoftickets)):
            myBuy = Buy(user=user,event=event,date='2015-07-08',purchase_id=purchasecode,trace_id=traceid)
            myBuy.save()
            Ticket.objects.filter(id=availticks[i][0]).update(free=1,buy=myBuy)
    except:
        pass

    return redirect('/main/')


@user_passes_test(lambda u: u.is_active and u.is_superuser)
def buymanager(request,eventid):

    events = Event.objects.filter(id=eventid)
    tickets = Ticket.objects.filter(event=events)
    name = events.values_list('name')[0][0]
    buy = tickets.values_list('buy')
    print(tickets)
    buys = []
    for i in range(len(buy)):
        if buy[i][0] is not None:
            buys.append(Buy.objects.filter(id=int(buy[i][0]))[0])

    return render(request,'buymanager.html',{'buys':buys,'name':name,'admin':True,'signed_in':True})


@login_required(redirect_field_name='/', login_url='/')
def add_to_cart(request,eventid):

    id = request.user.id
    myUser=models.User.objects.filter(id=id)
    user = User.objects.get(user=myUser)
    event = Event.objects.get(id=eventid)
    myCart = Cart(user=user,event=event,number=0)#needs attention
    myCart.save()

    return redirect('/main/')


@login_required(redirect_field_name='/', login_url='/')
def show_cart(request):
    id = request.user.id
    user = models.User.objects.filter(id=id)
    user = User.objects.filter(user=user)
    cart_list = Cart.objects.filter(user = user)
    totalprice = 0;
    for i in range(len(cart_list)):
        totalprice = totalprice + float(cart_list[i].event.ticket_price) * float(cart_list[i].number)
    if request.method == 'POST':
        for i in range(len(cart_list)):
            strname = str(cart_list[i].event.id)
            if request.POST.get(strname) is not None:
                total = float(request.POST.get(strname)) * float((cart_list[i].event.ticket_price))
                cart_list[i].number = int(request.POST.get(strname))
                totalprice = totalprice + total
    if cart_list.count() == 0:
        return render(request,'cart.html',{'carts':None,'totalprice':0})
    return render(request, 'cart.html', {'totalprice':totalprice,'carts' : cart_list})


@login_required(redirect_field_name='/', login_url='/')
def delete_cart(request, eventid):
    id = request.user.id
    djangouser = models.User.objects.filter(id=id)
    myuser = User.objects.filter(user=djangouser)
    event = Event.objects.filter(id=eventid)
    Cart.objects.filter(user=myuser, event=event).delete()
    return redirect('/cart/')

