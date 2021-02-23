from Alt_Career.settings import BASE_DIR
from rest_framework.views import APIView
from .options1 import industry_info, func_area_info
import os
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import itertools
import pandas as pd
import jsonify
from .predict import predict
from .dataprep import ind_dct, fun_dct, skill_dct, rolcat_dct, role_dct


def readiness(x, sk_inp):
    r = 0
    for i in sk_inp:
        if i in x:
            r = r + 1
    m = len(x)/len(sk_inp)
    m = r/m
    if r >= 0.7:
        t = [True, False, False]
        return t

    elif r >= 0.4:
        t = [False, True, False]
        return t

    else:
        t = [False, False, True]
        return t


class options_industry(APIView):
    def get(self, request):
        data = request.GET.get('industry')
        return industry_info(data)


class options_func(APIView):
    def get(self, request):
        func = request.GET.get('industry')
        func_area = request.GET.get('functional_area')
        return func_area_info(func, func_area)


def home(request):
    return render(request, 'homepage.html')


def result(request):
    if (request.method == 'POST'):
        
        ind_ = request.POST.get('industry')
        f_area_ = request.POST.get('functionalArea')
        sk1_ = request.POST.get('skill1')
        sk2_ = request.POST.get('skill2')
        sk3_ = request.POST.get('skill3')
        sk4_ = request.POST.get('skill4')
        sk5_ = request.POST.get('skill5')
        ind = ind_dct[ind_]
        f_area = fun_dct[f_area_]
        sk1 = skill_dct[sk1_]
        sk2 = skill_dct[sk2_]
        sk3 = skill_dct[sk3_]
        sk4 = skill_dct[sk4_]
        sk5 = skill_dct[sk5_]
        
        ready,final = predict.predict(ind,f_area,sk1,sk2,sk3,sk4,sk5,ind_,f_area_,sk1_,sk2_,sk3_,sk4_,sk5_)

        template = loader.get_template('jinja2/results.html')
        return HttpResponse(template.render(request, {'sen': final, 'tab': ready, 'itertools': itertools, 'jsonify': jsonify}))

