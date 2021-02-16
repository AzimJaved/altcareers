from django import template
from rest_framework.views import APIView
from .options1 import industry_info, func_area_info
from django.shortcuts import render

# from .dataprep import ind_dct, fun_dct, skill_dct, rolcat_dct, role_dct


class options_industry(APIView):
    def get(self, request):
        data = request.GET.get('industry')
        # print(data)
        return industry_info(data)


class options_func(APIView):
    def get(self, request):
        func = request.GET.get('industry')
        func_area = request.GET.get('functional_area')

        return func_area_info(func, func_area)


def home(request):
    return render(request, 'jinja2/homepage.html')


def result(request):
    return render(request, '')
