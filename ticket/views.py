from django.shortcuts import render, redirect
from ticket.models import Buy,Ticket,Cart
from event.models import Event
from account.models import User
from django.db import models
from django.contrib.auth import models
# Create your views here.
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
        mytick = Ticket.objects.filter(event=event,free=0)
        availticks = mytick.values_list('id')
    for i in range(int(numberoftickets)):
        myBuy = Buy(user=user,event=event,date='2015-07-08',purchase_id=purchasecode,trace_id=traceid)
        myBuy.save()
        Ticket.objects.filter(id=availticks[i][0]).update(free=1,buy=myBuy)

    return redirect('/main/')


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



def add_to_cart(request,eventid):

    # numberoftickets = request.POST.get("ticket_num")
    id = request.user.id
    myUser=models.User.objects.filter(id=id)
    user = User.objects.get(user=myUser)
    event = Event.objects.get(id=eventid)
    myCart = Cart(user=user,event=event,number=3)
    myCart.save()

    return redirect('/main/')


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
            total = float(request.POST.get(strname)) * float((cart_list[i].event.ticket_price))
            cart_list[i].number = int(request.POST.get(strname))
            totalprice = totalprice + total
    if cart_list.count() == 0:
        return render(request,'cart.html',{'carts':None,'totalprice':0})
    return render(request, 'cart.html', {'totalprice':totalprice,'carts' : cart_list})

def buy_cart(request):
    user = request.user
    cart_list = Cart.objects.filter(user__pk = user.pk)
    for cart in cart_list:
        userid = user.id
        eventid = cart.event.id
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
            mytick = Ticket.objects.filter(event=event,free=0)
            availticks = mytick.values_list('id')
            for i in range(int(numberoftickets)):
                myBuy = Buy(user=user,event=event,date='2015-07-08',purchase_id=purchasecode,trace_id=traceid)
                myBuy.save()
                Ticket.objects.filter(id=availticks[i][0]).update(free=1,buy=myBuy)

    return redirect('/main/')

