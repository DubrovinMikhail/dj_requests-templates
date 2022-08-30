from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


CONTENT = []
with open('data-398-2018-08-30.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        CONTENT.append(row)


def bus_stations(request):
    page = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    bus_stations = paginator.get_page(page)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': bus_stations.object_list,
        'page': bus_stations,
    }
    return render(request, 'stations/index.html', context)
