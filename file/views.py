from django.shortcuts import render
from django.views.generic import ListView

from file.models import File


class FileList(ListView):
    model = File
