import pandas as pd
import os
import json
from .settings import BASE_URL, BASE_DIR
import math
from itertools import permutations

# Loading useful dictionaries
with open(BASE_DIR + '/Alt_Career/csv/skills.json', 'r') as f:
    skill_dct = json.load(f)
with open(BASE_DIR + '/Alt_Career/csv/functional_area.json', 'r') as f:
    fun_dct = json.load(f)

with open(BASE_DIR + '/Alt_Career/csv/option.json', 'r') as f:
    options_dct = json.load(f)

with open(BASE_DIR + '/Alt_Career/csv/role.json', 'r') as f:
    role_dct = json.load(f)

with open(BASE_DIR + '/Alt_Career/csv/rolecat.json', 'r') as f:
    rolcat_dct = json.load(f)

with open(BASE_DIR + '/Alt_Career/csv/industry.json', 'r') as f:
    ind_dct = json.load(f)


def find_key(dct, value):
    '''
    Find key corresponding to the given value in the dct
    '''
    for key, val in dct.items():
        if val == value:
            return key


def jacard(x, sk_inp):
    '''
    Calculate jacard index for the given job role based on skills
    '''
    vec_input = []
    c = 0
    dot_prod = 0
    for param in sk_inp:
        if param in x:
            vec_input.append(1)
            c = c + 1
        else:
            vec_input.append(0)
    if c == 0:
        return 0
    vec_compare = [1, 1, 1, 1, 1, 1, 1]
    for i in range(len(vec_compare)):
        if vec_input[i] == 1:
            dot_prod = dot_prod + 1
    if dot_prod == 0:
        return 0
    mod_comp = math.sqrt(7)
    mod_vec = math.sqrt(c)
    jacard_index = dot_prod/(mod_vec*mod_comp)
    return jacard_index


def readiness(eligible_roles):
    '''
    Assign readiness metrics based on jacard index value
    '''
    ready = []
    for role in eligible_roles:
        r = role[1]
        if r >= 0.6:
            t = [True, False, False]
            ready.append(t)

        elif r >= 0.4:
            t = [False, True, False]
            ready.append(t)

        else:
            t = [False, False, True]
            ready.append(t)
    return ready


def predict(input_str, input_enc):
    #data = pd.read_csv(BASE_DIR + '/Alt_Career/csv/job_dataset.csv')
    data_enc = pd.read_csv(
        BASE_DIR + '/Alt_Career/csv/job_dataset_encoded.csv')

    input_combo = list(permutations(input_enc, 7))

    predicted_funcarea = []
    test = ['Skill1', 'Skill2', 'Skill3',
            'Skill4', 'Skill5', 'Skill6', 'Skill7']

    import pickle
    with open(BASE_DIR + '/Alt_Career/csv/model.pkl', 'rb') as file:
        forest = pickle.load(file)

    for x in input_combo:
        param = list(x)
        data_test = {}
        i = 0
        for col in test:
            data_test[col] = [param[i]]
            i = i+1
        test_df = pd.DataFrame(data_test)

        predict_code = forest.predict(test_df)
        predict_code = predict_code.tolist()

        if len(predict_code) > 0:
            for code in predict_code:
                if code is None:
                    continue
                else:
                    for key, value in fun_dct.items():
                        if value == code:
                            predicted_funcarea.append(key)
        else:
            continue
    # Unique functional areas in dataset
    funcarea = set(fun_dct.keys())
    predicted_funcarea = set(predicted_funcarea)
    # Get valid predicted func areas by checking for intersection with the original list of func areas
    predicted_funcarea.intersection_update(funcarea)
    # Predicted functional area(s)
    predicted_funcarea = list(predicted_funcarea)
    # Predicted functional area encoded values from fun_dct
    codes = []
    for x in predicted_funcarea:
        codes.append(fun_dct[x])

    # Generating 3d lists namely, senkey and table to draw the corresponding viz
    # senkey - [func area, job role, 5],[job role, skill, 5] --format[source node, destination node, value(thickness of senkey)]
    # table - [job role, True, False, False] --format-- [role, ready, mid term, long term] -- True/tick, False/cross

    if len(predicted_funcarea) > 0:
        senkey = []
        table = []
        for function in codes:
            fun_senkey = []
            role_ready = []
            roles_jacard = []
            data_fun = data_enc[data_enc['Functional Area'] == function]
            role_lt = list(set(data_fun['Role'].values))
            for r in role_lt:
                fun_senkey.append(
                    [find_key(fun_dct, function), find_key(role_dct, r), 5])
                data_role = data_fun[data_fun['Role'] == r]
                sc = ['Skill1', 'Skill2', 'Skill3',
                      'Skill4', 'Skill5', 'Skill6', 'Skill7']
                sk_count = {}
                for c in sc:
                    for skill in list(data_role[c].values):
                        sk_count[skill] = sk_count.get(skill, 0) + 1
                #count = sk_count.values()
                sort_dct = sorted(sk_count.items(),
                                  key=lambda ele: ele[1], reverse=True)
                sort_skill = [x[0] for x in sort_dct]
                # Find 7 mostt frequently occurring skills within the role in dataset
                top_skill = sort_skill[0:7]
                rol = find_key(role_dct, r)
                # Top skills will be used to calculate jacard's index
                # The integer codes will be used to calculate jacard's index to avoid discrepancies in accounting for similar skills
                d = [rol] + [jacard(top_skill, input_enc)]
                roles_jacard.append(d)
                role_ready.append(d)
                # Top skills will appear in senkey
                for sk in top_skill:
                    fun_senkey.append([rol, find_key(options_dct, sk), 5])
            # sorting the job roles according to suitability determined by high jacard's index value
            roles_jacard.sort(reverse=True, key=lambda x: x[1])
            role_ready = readiness(roles_jacard)
            table.append(role_ready)
            senkey.append(fun_senkey)

    return table, senkey
