from django.http import JsonResponse
from django.shortcuts import render
from job.models import Companies, TypeExpense, Data, Expenses
from django.views.decorators.csrf import csrf_protect, csrf_exempt


@csrf_exempt
def ajax(req):
    data = {"message": "successful ajax operation",
            "coming": req.POST.get("name")}
    return JsonResponse(data)


def filter(req):
    companies = Companies.objects.all()
    context = {
        "companies": companies,
    }
    if req.POST.get("receive"):
        receive = req.POST.get("receive")
        sender = req.POST.get("sender")
        value = req.POST.get("value")
        amount = req.POST.get("amount")
        distance = req.POST.get("distance")
        paid = req.POST.get("paid")
        paid = "true" if paid else "false"
        fee = req.POST.get("fee-type")
        weight = req.POST.get("amount-type")
        dist = req.POST.get("distance-type")
        context = {
            "companies": companies,
            "receive": receive,
            "sender": sender,
            "value": value,
            "amount": amount,
            "distance": distance,
            "paid": paid,
            "fee": fee,
            "weight": weight,
            "dist": dist,
        }
    return render(req, 'filter/test.html', context)
