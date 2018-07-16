from django.db import models

class Companies(models.Model):
    name = models.CharField(max_length=30)

class Data(models.Model):
    receive = models.ForeignKey(Companies, on_delete=models.CASCADE,related_name='receive')
    sender = models.ForeignKey(Companies, on_delete=models.CASCADE,related_name='sender')
    value=models.IntegerField()
    save_date = models.DateTimeField('save date')
    amount=models.IntegerField()
    distance=models.IntegerField()
    paid=models.BooleanField()
    detail = models.CharField(max_length=300)

class TypeExpense(models.Model):
    name = models.CharField(max_length=30)

class Expenses(models.Model):
    kind = models.ForeignKey(TypeExpense, on_delete=models.CASCADE)
    expense=models.IntegerField()
    detail = models.CharField(max_length=300)
    save_date = models.DateTimeField('save date')

