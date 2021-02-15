from django.shortcuts import render

# Create your views here.
from .options1 import industry_info, func_area_info
from rest_framework.views import APIView


class options_industry(APIView):
    def get(self, request):
        data = request.GET.get('industry')
        #print(data)
        return industry_info(data)


class options_func(APIView):
    def get(self, request):
        func = request.GET.get('industry')
        func_area = request.GET.get('functional_area')

        return func_area_info(func, func_area)



