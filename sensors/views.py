from django.shortcuts import render
from django.http import HttpResponse
from .models import Sensor, Data
from django.http import Http404

sensors_data = [
    {
        'sensor_id': 'GPIO 16',
        'date_time': '26.02.2020 18:08:01',
        'humidity': '46',
        'temperature': '23'
    },
    {
        'sensor_id': 'GPIO 16',
        'date_time': '26.02.2020 18:08:02',
        'humidity': '67',
        'temperature': '21'
    },
    {
        'sensor_id': 'GPIO 12',
        'date_time': '26.02.2020 18:08:03',
        '': '57',
        'temperature': '22'
    },
    {
        'sensor_id': 'GPIO 25',
        'date_time': '26.02.2020 18:08:05',
        'humidity': '69',
        'temperature': '23'
    },

]


def home(request):
    context = {
        'sensors': sensors_data
    }

    return render(request, 'sensors/home.html', context)

def about(request):
    return render(request, 'sensors/about.html', {'title': 'About'})

#def detail(request, sensor_id):
#    return HttpResponse("You're looking at sensors %s." % sensor_id)

def detail(request, sensor_id):
    try:
        data = Sensor.objects.get(pk=sensor_id)
    except Sensor.DoesNotExist:
        raise Http404("Unplugged")
    return render(request, 'sensors/detail.html', {'data': data, 'test': '123'})

def detail_index(request):
    return render(request, 'sensors/detail_index.html', {'title': "Sensors' List", 'test': '123'})

def pinout(request):
    return render(request, 'sensors/pinout.html', {'title': "Pinout", 'test': '123'})

