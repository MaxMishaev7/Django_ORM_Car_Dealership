from django.http import Http404
from django.shortcuts import render
from django.db import models

from .models import Car


def cars_list_view(request):
    # получите список авто
    cars = Car.objects.all()
    context = {
        'cars': cars,
    }
    template_name = 'main/list.html'
    # return render(request, template_name, {})  # передайте необходимый контекст
    return render(request, template_name, context)


def car_details_view(request, car_id):
    # получите авто, если же его нет, выбросьте ошибку 404
    template_name = 'main/details.html'
    return render(request, template_name, {})  # передайте необходимый контекст


def sales_by_car(request, car_id):
    try:
        # получите авто и его продажи
        template_name = 'main/sales.html'
        return render(request, template_name, {})  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
