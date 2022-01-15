from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Guest, Table
from django.utils import timezone
from datetime import datetime


class TableList(generic.ListView):

    def makebooking(self, request, *args, **kwargs):
        if request.method == "POST":
            form = Table(request.POST)
            if form.is_valid():
                form.save()
                return redirect('makebooking')
            queryset = Post.objects.filter(status=1)
            post = get_object_or_404(queryset)
            template_name = 'reservation.html'


