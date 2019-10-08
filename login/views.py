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
        to_get = fix_dots(to_get)
        query_columns = ",".join(to_get)    # Columns to select from DB

        # Fixing the field names inconsistency with columns names in DB


        # Fetching data from DB
        with connection.cursor() as cursor:
            query = 'select ' + query_columns + ' from student_info inner join sgpa_info on student_info.university_roll_no=sgpa_info.university_roll_no where ' + cond_query
            cursor.execute(query)
            data = list(cursor)
        
        if 'student_info.university_roll_no' in to_get:
            i = to_get.index('student_info.university_roll_no')
            to_get.insert(i,'university_roll_no')
            to_get.remove('student_info.university_roll_no')
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

    if 'min_sgpa' in cond:
        query += 'aggregate_sgpa>=\'{}\' AND '.format(cond['min_sgpa'])
    
    if 'max_backlogs' in cond:
        query += 'aggregate_sgpa<= \'{}\' AND '.format(cond['max_backlogs'])

    if not cond['gender_select'] == 'both':
        query += 'gender=\'{}\' AND '.format(cond['gender_select'])

    return cond,query


def fix_dots(arr):
#     for i in range(len(arr)):

#         arr[i] = arr[i].strip('_')
#         if 'contact' in arr[i].lower() or 'roll' in arr[i].lower():
#             arr[i] += '.'
        
#         arr[i] = arr[i].replace('_',' ')
#         arr[i] = '`{}`'.format(arr[i])
    if 'university_roll_no' in arr:
        arr.append('student_info.university_roll_no')
        arr.remove('university_roll_no')

    if 'address' in arr:
        arr.append('c_city_name')
        arr.remove('address')
    

    return arr

@login_required
def search(request):
    try:
        URN = request.POST['URN']
    
    except:
        return HttpResponse('404 Not Found')
    print(URN)
    search_query = 'Select student_info.university_roll_no,full_name,student_mobile_no,student_email,gender,aggregate_sgpa from student_info inner join sgpa_info on student_info.university_roll_no=sgpa_info.university_roll_no where student_info.university_roll_no=\'{}\''.format(URN)

    with connection.cursor() as cursor:
        cursor.execute(search_query)
        data = list(cursor)
    
    print(data)
    if data:
        context = {'data':data[0]}
    else:
        context = {}
    return render(request, 'view_data.html', context)


def serve_for_download():
    file_path = './data.xlsx'
    filename = 'data.xlsx'

    mime_type, _ = mimetypes.guess_type(file_path)
    with open(file_path, 'rb') as fl:
        response = HttpResponse(fl, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename={}".format(filename)

        return response
