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
    form2 = ConditionForm(request.POST or None)
    form3 = SearchForm(request.POST or None)

    if form1.is_valid() and form2.is_valid():

        to_get = [key for (key,val) in form1.cleaned_data.items() if val]
        conditions, cond_query = get_conditions(form2)
        cond_query += '1=1'

        # Fixing the field names inconsistency with columns names in DB
        fix_dots(to_get)

        query_columns = ",".join(to_get)    # Columns to select from DB

        # Fetching data from DB
        with connection.cursor() as cursor:
            query = 'select ' + query_columns + ' from Student where ' + cond_query
            cursor.execute(query)
            data = list(cursor)
        # Wriing data to excel file
        # wb = Workbook()
        # ws = wb.active
        # ws.append(to_get)
        # for i in data:
        #     ws.append(i)
        
        # wb.save('./data.xlsx')

        return render(request, 'view_before_download.html', {'to_get':to_get, 'data':data})

        # Serving the file for download
        

    return render(request,'home.html', {'form1':form1, 'form2':form2, 'form3':form3})



def get_conditions(form):

    cond = {key:val for (key,val) in form.cleaned_data.items() if val}

    query = ""

    if 'Aggregate_SGPA_OBTAINED' in cond:
        query += '`Aggregate SGPA OBTAINED`>=\'{}\' AND '.format(cond['Aggregate_SGPA_OBTAINED'])
    
    if 'XII_PERCENTAGE' in cond:
        query += '`XII PERCENTAGE`>=\'{}\' AND '.format(cond['XII_PERCENTAGE'])

    if 'X_PERCENTAGE' in cond:
        query += '`X PERCENTAGE`>=\'{}\' AND '.format(cond['X_PERCENTAGE'])
    
    if not cond['GENDER'] == 'both':
        query += 'GENDER=\'{}\' AND '.format(cond['GENDER'])

    return cond,query


def fix_dots(arr):
    for i in range(len(arr)):

        arr[i] = arr[i].strip('_')
        if 'contact' in arr[i].lower() or 'roll' in arr[i].lower():
            arr[i] += '.'
        
        arr[i] = arr[i].replace('_',' ')
        arr[i] = '`{}`'.format(arr[i])

@login_required
def search(request):
    try:
        URN = request.POST['URN']
    
    except:
        return HttpResponse('404 Not Found')
    print(URN)
    search_query = 'Select `UNIVERSITY ROLL NO.`,`FULL NAME`,`STUDENTS CONTACT NO.`,`EMAIL ADDRESS`,`GENDER`,`X PERCENTAGE`,`XII PERCENTAGE`,`Aggregate SGPA OBTAINED` from Student where `UNIVERSITY ROLL NO.`=\'{}\''.format(URN)

    with connection.cursor() as cursor:
        cursor.execute(search_query)
        data = list(cursor)
    
    print(data)
    return render(request, 'view_data.html', {'data':data[0]})


def serve_for_download():
    file_path = './data.xlsx'
    filename = 'data.xlsx'

    mime_type, _ = mimetypes.guess_type(file_path)
    with open(file_path, 'rb') as fl:
        response = HttpResponse(fl, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename={}".format(filename)

        return response
