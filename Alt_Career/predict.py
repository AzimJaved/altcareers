import pandas as pd
import os
import json
from .settings import BASE_URL, BASE_DIR
import math
from itertools import permutations

<<<<<<< HEAD

#Loading useful dictionaries
with open(BASE_DIR + '/Alt_Career/csv/skills.json','r') as f:
    skill_dct = json.load(f)
with open(BASE_DIR + '/Alt_Career/csv/functional_area.json','r') as f:
    fun_dct = json.load(f)

with open(BASE_DIR + '/Alt_Career/csv/option.json','r') as f:
    options_dct = json.load(f)

with open(BASE_DIR + '/Alt_Career/csv/role.json','r') as f:
    role_dct = json.load(f)

with open(BASE_DIR + '/Alt_Career/csv/rolecat.json','r') as f:
    rolcat_dct = json.load(f)

with open(BASE_DIR + '/Alt_Career/csv/industry.json','r') as f:
    ind_dct = json.load(f)

def find_key(dct,value):
    '''
    Find key corresponding to the given value in the dct
    '''
    for key,val in dct.items():
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
    vec_compare = [1,1,1,1,1,1,1]
    for i in range(len(vec_compare)):
        if vec_input[i] == 1:
            dot_prod = dot_prod + 1
    if dot_prod == 0:
        return 0
    mod_comp = math.sqrt(7)
    mod_vec = math.sqrt(c)
    jacard_index = dot_prod/(mod_vec*mod_comp)
    return jacard_index
=======
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

def predict(ind,f_area,sk1,sk2,sk3,sk4,sk5,ind_,f_area_,sk1_,sk2_,sk3_,sk4_,sk5_):
    data = pd.read_csv(BASE_DIR + '/Alt_Career/csv/job_dataset.csv')
    data_enc = pd.read_csv(BASE_DIR + '/Alt_Career/csv/job_dataset_encoded.csv')
    
    data_new = data_enc[(data_enc['Industry'] == ind) & (data_enc['Functional Area'] == f_area)]
    y = data_new['Role Category']
    X = data_new[['Industry','Functional Area','Skill1','Skill2','Skill3','Skill4','Skill5']]
    if len(data_new)>20:
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state =42)
        #from sklearn.metrics import classification_report ,f1_score,accuracy_score,confusion_matrix,precision_score, recall_score
        from sklearn.ensemble import RandomForestClassifier

        forest=RandomForestClassifier()
        forest.fit(X_train,y_train)

        y_pred=forest.predict(X_test)
    else:
        from sklearn.ensemble import RandomForestClassifier
        forest=RandomForestClassifier()
        forest.fit(X, y)

        y_pred=forest.predict(X)
    
    predicted_rolecat = []
    test = ['Industry', 'Functional Area', 'Skill1',
            'Skill2', 'Skill3', 'Skill4', 'Skill5']
    param = [f_area, ind, sk1, sk2, sk3, sk4, sk5]
    data_test = {}
    i = 0
    for col in test:
        data_test[col] = [param[i]]
        i = i+1
    # data_test
    test_df = pd.DataFrame(data_test)

    test = ['Industry', 'Functional Area', 'Skill1',
            'Skill2', 'Skill3', 'Skill4', 'Skill5']
    param = [f_area, ind, sk1, sk2, sk3, sk4, sk5]
    data_test = {}
    i = 0
    for col in test:
        data_test[col] = [param[i]]
        i = i+1
    # data_test
    test_df = pd.DataFrame(data_test)

    predict_code = forest.predict(test_df)
    predict_code = predict_code.tolist()
    # print(predict_code)
    for code in predict_code:
        if code is None:
            print("No role predicted")
            break
        else:
            for key, value in rolcat_dct.items():
                if value == code:
                    predicted_rolecat.append(key)
    # print(predicted_rolecat)
    fin = []
    rolecat = rolcat_dct.keys()
    for rc in predicted_rolecat:
        if rc in rolecat:
            fin.append(rc)
        else:
            pass
    predicted_rolecat = list(set(fin))
    final = []
    ready = []
    sk_inp = [sk1_, sk2_, sk3_, sk4_, sk5_]
    # print(predicted_rolecat)
    if len(predicted_rolecat) > 0:
        for rol_cat in predicted_rolecat:
            data2 = data[(data['Role Category'] == rol_cat)]
            #display(data2)
            #ind_lt = list(set(data2['Industry'].values))
            d1 = []
            #for i in ind_lt:
            intermed = []
            #intermed.append([rol_cat,i,3])
            #data3 = data2[data2['Industry'] == i]
            role_lt = list(set(list(data2['Role'].values)))
            for role in role_lt:
                intermed.append([rol_cat, role, 4])
            for role in role_lt :
                data4 = data2[data2['Role'] == role]
                sc = ['Skill1','Skill2','Skill3','Skill4','Skill5']
                sk_dct = {}
                for c in sc:
                    for skill in list(data4[c].values):
                        sk_dct[skill] = sk_dct.get(skill, 0) + 1
                count = list(sk_dct.values())
                sort_dct = sorted(sk_dct.items(), key = lambda ele: ele[1], reverse = True)
                sort_skill = [x[0] for x in sort_dct]
                #print(sort_dct)
                if max(count) < 5:
                    b = sort_skill[0:30]
                else:
                    b = sort_skill[0:20]
                d = [role] + readiness(b, sk_inp)
                d1.append(d)
                top_skill = b[0:5]
                for sk in top_skill:
                    unique = " " + str(sk) + " "
                    intermed.append([role, unique, 4])
            final.append(intermed)
            ready.append(d1)
>>>>>>> 83e2dc22ee4c3f68deb83e1cd598d1adce045711



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

        elif r >= 0.4 :
            t=[False, True, False]
            ready.append(t)

        else :
            t=[False, False, True]
            ready.append(t)
    return ready


def predict(input_str, input_enc):
    #data = pd.read_csv(BASE_DIR + '/Alt_Career/csv/job_dataset.csv')
    data_enc = pd.read_csv(BASE_DIR + '/Alt_Career/csv/job_dataset_encoded.csv')
    
    input_combo = list(permutations(input_enc,7))

    predicted_funcarea = []
    test = ['Skill1','Skill2','Skill3','Skill4','Skill5', 'Skill6','Skill7']

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
        
        if len(predict_code)>0:
            for code in predict_code:
                if code is None:
                    continue
                else:
                    for key,value in fun_dct.items():
                        if value == code:
                            predicted_funcarea.append(key)
        else:
            continue
    #Unique functional areas in dataset
    funcarea = set(fun_dct.keys())
    predicted_funcarea = set(predicted_funcarea)
    #Get valid predicted func areas by checking for intersection with the original list of func areas
    predicted_funcarea.intersection_update(funcarea)
    #Predicted functional area(s)
    predicted_funcarea = list(predicted_funcarea)
    #Predicted functional area encoded values from fun_dct
    codes = []
    for x in predicted_funcarea:
        codes.append(fun_dct[x])

    #Generating 3d lists namely, senkey and table to draw the corresponding viz
    #senkey - [func area, job role, 5],[job role, skill, 5] --format[source node, destination node, value(thickness of senkey)]
    #table - [job role, True, False, False] --format-- [role, ready, mid term, long term] -- True/tick, False/cross

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
                fun_senkey.append([find_key(fun_dct,function),find_key(role_dct,r),5])
                data_role = data_fun[data_fun['Role'] == r]
                sc = ['Skill1','Skill2','Skill3','Skill4','Skill5','Skill6','Skill7']
                sk_count = {}
                for c in sc:
                    for skill in list(data_role[c].values):
                        sk_count[skill] = sk_count.get(skill, 0) + 1
                #count = sk_count.values()
                sort_dct = sorted(sk_count.items(), key = lambda ele: ele[1], reverse = True)
                sort_skill = [x[0] for x in sort_dct]
                #Find 7 mostt frequently occurring skills within the role in dataset
                top_skill = sort_skill[0:7]
                rol = find_key(role_dct,r)
                #Top skills will be used to calculate jacard's index
                #The integer codes will be used to calculate jacard's index to avoid discrepancies in accounting for similar skills
                d = [rol] + [jacard(top_skill, input_enc)]
                roles_jacard.append(d)
                role_ready.append(d)
                #Top skills will appear in senkey
                for sk in top_skill:
                    fun_senkey.append([rol, find_key(options_dct,sk), 5])
            #sorting the job roles according to suitability determined by high jacard's index value
            roles_jacard.sort(reverse=True,key = lambda x: x[1])
            role_ready = readiness(roles_jacard)
            table.append(role_ready)
            senkey.append(fun_senkey)
    
    return table,senkey