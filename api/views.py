from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class Blogs(View):
    def get(self, request):
        return HttpResponse("hi")