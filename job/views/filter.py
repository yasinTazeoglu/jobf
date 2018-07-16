from django.shortcuts import render
from job.models import Data, Expenses, Companies
from django.utils import timezone


def data(req):
    # allData=Data.objects.order_by('paid','distance')
    allData = Data.objects.all().reverse()
    myData = Data.objects.filter(save_date__minute__gt=8).filter(paid=False)
    companies = Companies.objects.all()
    context = {
        "companies": companies,
        # "allData":myData
    }
    if req.POST.get("receive"):
        return datafilter(req)
    else:
        return render(req, 'filter/data.html', context)


def expense(req):
    # allData=Data.objects.order_by('paid','distance')
    allData = Expenses.objects.all()
    # myData=Expenses.objects.filter(save_date__minute__gt=8).filter(paid=False)
    context = {
        "allData": allData
        # "allData":myData
    }
    return render(req, 'filter/expense.html', context)


def datafilter(req):
    myData = Data.objects.all()
    receive = req.POST.get("receive")
    myData=cp("receive",receive,myData)

    sender = req.POST.get("sender")
    myData=cp("sender",sender,myData)

    fee = req.POST.get("fee-type")
    value = req.POST.get("value")
    myData=bes(fee,myData,value,"value")

    weight = req.POST.get("amount-type")
    amount = req.POST.get("amount")
    myData=bes(weight,myData,amount,"amount")

    dist = req.POST.get("distance-type")
    distance = req.POST.get("distance")
    myData=bes(dist,myData,distance,"distance")

    paid=req.POST.get("paid")
    if paid=="2":
        myData = myData.filter(paid=False)
    elif paid == "3":
        myData=myData.filter(paid=True)
    context = {
        "allData": myData,
    }
    return render(req, 'filter/elementPage.html', context)

def bes(t,m,v,n):
    f={}
    mf=n
    if t == "1":
        mf+="__gt"
    elif t == "3":
        mf+="__lt"
    f[mf]=v
    return m.filter(**f)
def cp(n,v,m):
    mm=m
    if v !="all":
        o={}
        mc=Companies.objects.get(pk=v)
        o[n]=v
        mm=m.filter(**o)
    return mm
    
