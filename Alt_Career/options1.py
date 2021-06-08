import pandas as pd
import json
import os
from rest_framework import status
from django.http import JsonResponse
from .settings import BASE_URL, BASE_DIR




def skill0_info():
    with open(BASE_DIR + '/Alt_Career/csv/skills.json','r') as f:
        skills_dct = json.load(f)
    data_enc = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_encoded.csv")
    #m_enc = list(set(data_enc['Skill1'].values))
    #m_enc = list(set(skills_dct.keys()))
    # code = options_dct[s1]
    # if code in m_enc:
    #     m_enc.remove(code)
    info_dct = list(set(skills_dct.keys()))
    return JsonResponse({"data": info_dct}, status=status.HTTP_200_OK)

def skill1_info(s1):
    with open(BASE_DIR + '/Alt_Career/csv/skills.json','r') as f:
        skills_dct = json.load(f)
    #data_enc = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_encoded.csv")
    #m_enc = list(set(data_enc['Skill2'].values))
    #m_enc = list(set(skills_dct.values()))
    #code = skills_dct[s1]
    #if code in m_enc:
    #    m_enc.remove(code)
    del skills_dct[s1]
    info_dct = list(set(skills_dct.keys()))
    return JsonResponse({"data": info_dct}, status=status.HTTP_200_OK)


def skill2_info(s1, s2):
    with open(BASE_DIR + '/Alt_Career/csv/skills.json','r') as f:
        skills_dct = json.load(f)
    #data_enc = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_encoded.csv")
    #m_enc = list(set(data_enc['Skill3'].values))
    code = [s1, s2]
    for s in code:
        del skills_dct[s]
    info_dct = list(set(skills_dct.keys()))
    return JsonResponse({"data": info_dct}, status=status.HTTP_200_OK)

def skill3_info(s1, s2, s3):
    with open(BASE_DIR + '/Alt_Career/csv/skills.json','r') as f:
        skills_dct = json.load(f)
    #data_enc = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_encoded.csv")
    #m_enc = list(set(data_enc['Skill3'].values))
    code = [s1, s2, s3]
    for s in code:
        del skills_dct[s]
    info_dct = list(set(skills_dct.keys()))
    return JsonResponse({"data": info_dct}, status=status.HTTP_200_OK)

def skill4_info(s1, s2, s3, s4):
    with open(BASE_DIR + '/Alt_Career/csv/skills.json','r') as f:
        skills_dct = json.load(f)
    #data_enc = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_encoded.csv")
    #m_enc = list(set(data_enc['Skill3'].values))
    code = [s1, s2, s3, s4]
    for s in code:
        del skills_dct[s]
    info_dct = list(set(skills_dct.keys()))
    return JsonResponse({"data": info_dct}, status=status.HTTP_200_OK)

def skill5_info(s1, s2, s3, s4, s5):
    with open(BASE_DIR + '/Alt_Career/csv/skills.json','r') as f:
        skills_dct = json.load(f)
    #data_enc = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_encoded.csv")
    #m_enc = list(set(data_enc['Skill3'].values))
    code = [s1, s2, s3, s4, s5]
    for s in code:
        del skills_dct[s]
    info_dct = list(set(skills_dct.keys()))
    return JsonResponse({"data": info_dct}, status=status.HTTP_200_OK)

def skill6_info(s1, s2, s3, s4, s5, s6):
    with open(BASE_DIR + '/Alt_Career/csv/skills.json','r') as f:
        skills_dct = json.load(f)
    #data_enc = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_encoded.csv")
    #m_enc = list(set(data_enc['Skill3'].values))
    code = [s1, s2, s3, s4, s5, s6]
    for s in code:
        del skills_dct[s]
    info_dct = list(set(skills_dct.keys()))
    return JsonResponse({"data": info_dct}, status=status.HTTP_200_OK)
