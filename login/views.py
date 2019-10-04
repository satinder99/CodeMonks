from django.shortcuts import render
from .forms import DataForm, ConditionForm, SearchForm
import mimetypes
from django.http import HttpResponse
from django.db import connection
from openpyxl import Workbook
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home_page(request):

    form1 = DataForm(request.POST or None)

    if form1.is_valid():
        to_get = [key for (key,val) in form1.cleaned_data.items() if val]
        # Fixing the field names inconsistency with columns names in DB
        fix_dots(to_get)

        query_columns = ",".join(to_get)    # Columns to select from DB

        # Fetching data from DB
        with connection.cursor() as cursor:
            query = 'select ' + query_columns + ' from Student'
            cursor.execute(query)
            data = list(cursor)
        # Wriing data to excel file
        wb = Workbook()
        ws = wb.active
        ws.append(to_get)
        for i in data:
            ws.append(i)
        
        wb.save('./data.xlsx')

        

    return render(request,'home.html', {'form1':form1, 'form2':form2, 'form3':form3})


def fix_dots(arr):
    for i in range(len(arr)):

        arr[i] = arr[i].strip('_')
        if 'contact' in arr[i].lower() or 'roll' in arr[i].lower():
            arr[i] += '.'
        
        arr[i] = arr[i].replace('_',' ')
        arr[i] = '`{}`'.format(arr[i])

