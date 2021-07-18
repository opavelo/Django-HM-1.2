from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
import csv
import os
from pprint import pprint


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    link = 'C:/Users/Pavel/Desktop/Обучение Phyton/Нетология/Django/Homework/1.2-requests-templates/pagination/data-398-2018-08-30.csv'
    context = []
    with open(link, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        context.append('Name, ' + 'Street, ' + 'District')
        for row in reader:
            # context.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
            context.append(row['Name'] + ', ' + row['Street'] + ', ' + row['District'])

    #pprint(context)
    page = int(request.GET.get('page', 1))
    elements_per_page = 100
    paginator = Paginator(context, elements_per_page)
    page_ = paginator.get_page(page)
    context = page_.object_list
    return HttpResponse('<br>'.join(context))


    # context = {
    # #     'bus_stations': ...,
    # #     'page': ...,
    # }
    # return render(request, 'stations/index.html', context)

# bus_stations()