from django.shortcuts import render
from job.models import Companies, TypeExpense, Data, Expenses
from django.utils import timezone


def companies(req):
    allcompany = Companies.objects.all()
    context = {"allcompany":allcompany}
    if req.method == 'POST':
        saveName = req.POST.get("name")
        company = Companies(name=saveName)
        company.save()
    return render(req, 'save/companies.html', context)


def data(req):
    context = {
        "type": "save/data",
        "companies": Companies.objects.all()
    }
    if req.method == 'POST':
        receive = Companies.objects.get(pk=req.POST.get("receive"))
        sender = Companies.objects.get(pk=req.POST.get("sender"))
        value = req.POST.get("value")
        amount = req.POST.get("amount")
        distance = req.POST.get("distance")
        paid = req.POST.get("paid") == "True"
        detail = req.POST.get("detail")
        save_date = timezone.now()
        data = Data(receive=receive, sender=sender, value=value, save_date=save_date,
                    amount=amount, distance=distance, paid=paid, detail=detail)
        data.save()

    return render(req, 'save/data.html', context)


def expense(req):
    context = {
        "type": "save/expense",
        "expenses": TypeExpense.objects.all()
    }
    if req.method == "POST":
        kind = TypeExpense.objects.get(pk=req.POST.get("kind"))
        detail = req.POST.get("detail")
        expense = req.POST.get("expense")
        Expenses(kind=kind, expense=expense, detail=detail,
                 save_date=timezone.now()).save()

    return render(req, 'save/expense.html', context)


def typeofexpense(req):
    allexpesnsetype= TypeExpense.objects.all()
    context = {
        "allexpensetype":allexpesnsetype
    }
    if req.method == 'POST':
        saveName = req.POST.get("name")
        company = TypeExpense(name=saveName)
        company.save()
    return render(req, 'save/typeofexpense.html', context)
