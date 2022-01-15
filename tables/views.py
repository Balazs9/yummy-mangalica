from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Guest, Table, Size
from django.utils import timezone
from datetime import datetime


def reseravtion(request):
    return render(request, 'reservation.html')


class TableList(View):
    
    def get(self, request, *args, **kwargs):
        queryset = Guest.objects.filter(Guest)
        post = get_object_or_404(queryset)