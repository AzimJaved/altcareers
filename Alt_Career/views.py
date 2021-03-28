from Alt_Career.settings import BASE_DIR
from rest_framework.views import APIView
from .options1 import skill1_info, skill2_info, skill3_info, skill4_info, skill5_info, skill6_info
import os
import json
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import itertools
import pandas as pd
import jsonify
from .predict import predict

#Loading useful dictionaries
with open(BASE_DIR + '/Alt_Career/csv/skills.json','r') as f:
    skill_dct = json.load(f)


class options_skill1(APIView):
    def get(self, request):
        param1 = request.GET.get('skill1')
        return skill1_info(param1)


class options_skill2(APIView):
    def get(self, request):
        param1 = request.GET.get('skill1')
        param2 = request.GET.get('skill2')
        return skill2_info(param1, param2)

class options_skill3(APIView):
    def get(self, request):
        param1 = request.GET.get('skill1')
        param2 = request.GET.get('skill2')
        param3 = request.GET.get('skill3')
        return skill3_info(param1, param2, param3)

class options_skill4(APIView):
    def get(self, request):
        param1 = request.GET.get('skill1')
        param2 = request.GET.get('skill2')
        param3 = request.GET.get('skill3')
        param4 = request.GET.get('skill4')
        return skill4_info(param1, param2, param3, param4)

class options_skill5(APIView):
    def get(self, request):
        param1 = request.GET.get('skill1')
        param2 = request.GET.get('skill2')
        param3 = request.GET.get('skill3')
        param4 = request.GET.get('skill4')
        param5 = request.GET.get('skill5')
        return skill5_info(param1, param2, param3, param4, param5)

class options_skill6(APIView):
    def get(self, request):
        param1 = request.GET.get('skill1')
        param2 = request.GET.get('skill2')
        param3 = request.GET.get('skill3')
        param4 = request.GET.get('skill4')
        param5 = request.GET.get('skill5')
        param6 = request.GET.get('skill6')
        return skill6_info(param1, param2, param3, param4, param5, param6)


def home(request):
    return render(request, 'homepage.html')


def result(request):
    if (request.method == 'POST'):
        
        sk1_ = request.POST.get('skill1')
        sk2_ = request.POST.get('skill2')
        sk3_ = request.POST.get('skill3')
        sk4_ = request.POST.get('skill4')
        sk5_ = request.POST.get('skill5')
        sk6_ = request.POST.get('skill6')
        sk7_ = request.POST.get('skill7')
        sk1 = skill_dct[sk1_]
        sk2 = skill_dct[sk2_]
        sk3 = skill_dct[sk3_]
        sk4 = skill_dct[sk4_]
        sk5 = skill_dct[sk5_]
        sk6 = skill_dct[sk6_]
        sk7 = skill_dct[sk7_]
        
        input_str = [sk1_,sk2_,sk3_,sk4_,sk5_,sk6_,sk7_]
        input_enc = [sk1, sk2, sk3, sk4, sk5, sk6, sk7]

        ready,final = predict(input_str,input_enc)
        
        return render(request, 'results.html', {'sen': final, 'tab': ready, 'sen_tab': itertools.zip_longest(final, ready, range(0, len(final)))})
        #template = loader.get_template('jinja2/results.html')
        #return HttpResponse(template.render(request, {'sen': final, 'tab': ready, 'itertools': itertools, 'jsonify': jsonify}))

