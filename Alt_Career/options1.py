import pandas as pd
import numpy as np
import json
import os
from rest_framework import status
from django.http import JsonResponse
from .settings import BASE_URL, BASE_DIR
import csv

with open(BASE_DIR + '/Alt_Career/csv/option.json','r') as f:
    options_dct = json.load(f)

def skill1_info(s1):
    data_enc = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_encoded.csv")
    m_enc = list(set(data_enc['Skill2'].values))
    code = options_dct[s1]
    if code in m_enc:
        m_enc.remove(code)
    info_dct = [key for key,val in options_dct if val in m_enc]
    return JsonResponse({"data": info_dct}, status=status.HTTP_200_OK)


def skill2_info(s1, s2):
    data_enc = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_encoded.csv")
    m_enc = list(set(data_enc['Skill3'].values))
    code = [options_dct[s1], options_dct[s2]]
    for c in code:
        if c in m_enc:
            m_enc.remove(c)
    info_dct = [key for key,val in options_dct if val in m_enc]
    return JsonResponse({"data": info_dct}, status=status.HTTP_200_OK)

def skill3_info(s1, s2, s3):
    data_enc = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_encoded.csv")
    m_enc = list(set(data_enc['Skill4'].values))
    code = [options_dct[s1], options_dct[s2], options_dct[s3]]
    for c in code:
        if c in m_enc:
            m_enc.remove(c)
    info_dct = [key for key,val in options_dct if val in m_enc]
    return JsonResponse({"data": info_dct}, status=status.HTTP_200_OK)

def skill4_info(s1, s2, s3, s4):
    data_enc = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_encoded.csv")
    m_enc = list(set(data_enc['Skill5'].values))
    code = [options_dct[s1], options_dct[s2], options_dct[s3], options_dct[s4]]
    for c in code:
        if c in m_enc:
            m_enc.remove(c)
    info_dct = [key for key,val in options_dct if val in m_enc]
    return JsonResponse({"data": info_dct}, status=status.HTTP_200_OK)

def skill5_info(s1, s2, s3, s4, s5):
    data_enc = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_encoded.csv")
    m_enc = list(set(data_enc['Skill6'].values))
    code = [options_dct[s1], options_dct[s2], options_dct[s3], options_dct[s4], options_dct[s5]]
    for c in code:
        if c in m_enc:
            m_enc.remove(c)
    info_dct = [key for key,val in options_dct if val in m_enc]
    return JsonResponse({"data": info_dct}, status=status.HTTP_200_OK)

def skill6_info(s1, s2, s3, s4, s5, s6):
    data_enc = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_encoded.csv")
    m_enc = list(set(data_enc['Skill7'].values))
    code = [options_dct[s1], options_dct[s2], options_dct[s3], options_dct[s4], options_dct[s5], options_dct[s6]]
    for c in code:
        if c in m_enc:
            m_enc.remove(c)
    info_dct = [key for key,val in options_dct if val in m_enc]
    return JsonResponse({"data": info_dct}, status=status.HTTP_200_OK)
