import pandas as pd
import numpy as np
import json
import os
from rest_framework import status
from django.http import JsonResponse
from .settings import BASE_URL, BASE_DIR
import csv

with open(BASE_DIR + '/Alt_Career/csv/skills.json','r') as f:
    skills_dct = json.load(f)

def skill0_info():
    data_enc = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_encoded.csv")
    m_enc = list(set(data_enc['Skill1'].values))
    # code = options_dct[s1]
    # if code in m_enc:
    #     m_enc.remove(code)
    info_dct = [key for key,val in skills_dct.items()]
    return JsonResponse({"data": info_dct}, status=status.HTTP_200_OK)

def skill1_info(s1):
    data_enc = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_encoded.csv")
    m_enc = list(set(data_enc['Skill2'].values))
    code = skills_dct[s1]
    if code in m_enc:
        m_enc.remove(code)
    info_dct = [key for key,val in skills_dct.items() if val in m_enc]
    return JsonResponse({"data": info_dct}, status=status.HTTP_200_OK)


def skill2_info(s1, s2):
    data_enc = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_encoded.csv")
    m_enc = list(set(data_enc['Skill3'].values))
    code = [skills_dct[s1], skills_dct[s2]]
    for c in code:
        if c in m_enc:
            m_enc.remove(c)
    info_dct = [key for key,val in skills_dct.items() if val in m_enc]
    return JsonResponse({"data": info_dct}, status=status.HTTP_200_OK)

def skill3_info(s1, s2, s3):
    data_enc = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_encoded.csv")
    m_enc = list(set(data_enc['Skill4'].values))
    code = [skills_dct[s1], skills_dct[s2], skills_dct[s3]]
    for c in code:
        if c in m_enc:
            m_enc.remove(c)
    info_dct = [key for key,val in skills_dct.items() if val in m_enc]
    return JsonResponse({"data": info_dct}, status=status.HTTP_200_OK)

def skill4_info(s1, s2, s3, s4):
    data_enc = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_encoded.csv")
    m_enc = list(set(data_enc['Skill5'].values))
    code = [skills_dct[s1], skills_dct[s2], skills_dct[s3], skills_dct[s4]]
    for c in code:
        if c in m_enc:
            m_enc.remove(c)
    info_dct = [key for key,val in skills_dct.items() if val in m_enc]
    return JsonResponse({"data": info_dct}, status=status.HTTP_200_OK)

def skill5_info(s1, s2, s3, s4, s5):
    data_enc = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_encoded.csv")
    m_enc = list(set(data_enc['Skill6'].values))
    code = [skills_dct[s1], skills_dct[s2], skills_dct[s3], skills_dct[s4], skills_dct[s5]]
    for c in code:
        if c in m_enc:
            m_enc.remove(c)
    info_dct = [key for key,val in skills_dct.items() if val in m_enc]
    return JsonResponse({"data": info_dct}, status=status.HTTP_200_OK)

def skill6_info(s1, s2, s3, s4, s5, s6):
    data_enc = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_encoded.csv")
    m_enc = list(set(data_enc['Skill7'].values))
    code = [skills_dct[s1], skills_dct[s2], skills_dct[s3], skills_dct[s4], skills_dct[s5], skills_dct[s6]]
    for c in code:
        if c in m_enc:
            m_enc.remove(c)
    info_dct = [key for key,val in skills_dct.items() if val in m_enc]
    return JsonResponse({"data": info_dct}, status=status.HTTP_200_OK)
