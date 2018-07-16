from django.contrib import admin
from .models import Companies,Expenses,Data,TypeExpense

admin.site.register(Companies)
admin.site.register(Expenses)
admin.site.register(Data)
admin.site.register(TypeExpense)