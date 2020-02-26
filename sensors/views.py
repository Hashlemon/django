from django.shortcuts import render
from django.http import HttpResponse

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

