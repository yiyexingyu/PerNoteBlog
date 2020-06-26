from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.


class Index(View):

    def get(self, request):
        print("request type: ", request)
        return render(request, 'index.html')

