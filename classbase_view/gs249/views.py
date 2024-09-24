from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def myview(request):
    return HttpResponse("<h1> function base view </h1>")


#class base view

class CLbaseView(View):
    name = "Ranjit"
    def get(self, request):
        # return HttpResponse("<h1> Classbase view </h1>")
        return HttpResponse(self.name)
