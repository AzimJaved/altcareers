import pandas as pd
import numpy as np
import json
import os
from rest_framework import status
from django.http import JsonResponse
from .settings import BASE_URL, BASE_DIR
import csv


def industry_info(industry):
    import pandas as pd
    #inds = str(industry)
    #print(industry)
    data = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset.csv")
    #print(data.head())
    #data_ind = data[data['Industry'] == industry]
    opt = [industry]
    data_ind = data[data['Industry'].isin(opt)]
    print(data_ind)
    #print(data["Industry"])
    info_dct = {}
    ind_farea = list(set(list(data_ind['Functional Area'].values)))
    info_dct[industry] = ind_farea
    # dct = json.dumps(info_dct)
    return JsonResponse({"data": info_dct}, status=status.HTTP_200_OK)


def func_area_info(industry, functional_area):
    data = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset.csv")
    sk_col = ["Skill1","Skill2","Skill3","Skill4","Skill5"]
    data_indfunc = data[(data['Industry'] == industry) & (data['Functional Area'] == functional_area)]
    info_dct = {}
    info_dct[functional_area] = {key : list(set(list(data_indfunc[key].values))) for key in sk_col}
    #dct = json.dumps(info_dct)
    return JsonResponse({"data": info_dct}, status=status.HTTP_200_OK)
