from django.urls import path
from .views import save,filter,test
urlpatterns=[
    path('', save.data,name='index'),
    path('save/companies',save.companies,name='companies'),
    path('save/expense',save.expense,name='expense'),
    path('save/type/expense',save.typeofexpense,name='typeofexpense'),
    path('filter/data',filter.data,name='filterdata'),
    path('filter/expense',filter.expense,name='filterexpense'),
    path('ajax/test/',test.ajax,name='ajax'),
]