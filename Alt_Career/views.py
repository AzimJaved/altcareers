from Alt_Career.settings import BASE_DIR
from rest_framework.views import APIView
from .options1 import industry_info, func_area_info

from django.http import HttpResponse
from django.template import loader
import itertools
import pandas as pd
import jsonify
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
        # print(data)
        return industry_info(data)


class options_func(APIView):
    def get(self, request):
        func = request.GET.get('industry')
        func_area = request.GET.get('functional_area')

        return func_area_info(func, func_area)


def home(request):
    template = loader.get_template('jinja2/homepage.html')
    context = {
        'latest_question_list': '',
    }
    return HttpResponse(template.render(context))


def result(request):
    if (request.method == 'POST'):
        data = pd.read_csv(BASE_DIR + '/Alt_Career/csv/job_dataset.csv')
        data_enc = pd.read_csv(BASE_DIR + '/Alt_Career/csv/job_dataset_encoded.csv')
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

        data_test = data_enc[(data_enc['Industry'] == ind) & (
            data_enc['Functional Area'] == f_area)]
        y = data_test['Role Category']
        X = data_test[['Industry', 'Functional Area',
                       'Skill1', 'Skill2', 'Skill3', 'Skill4', 'Skill5']]
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, train_size=0.8, test_size=0.2, random_state=42)
        from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix, precision_score, recall_score
        from sklearn.ensemble import RandomForestClassifier

        forest = RandomForestClassifier()
        forest.fit(X_train, y_train)

        y_pred = forest.predict(X_test)

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
                data2 = data[(data['Role Category'] == rol_cat) & (
                    data['Functional Area'] == f_area_) & (data['Industry'] == ind_)]
                # display(data2)
                role_lt = []
                intermed = []
                d1 = []
                role_lt = list(set(list(data2['Role'].values)))
                for role in role_lt:
                    intermed.append([rol_cat, role, 5])
                for role in role_lt:
                    data3 = data2[data2['Role'] == role]
                    sc = ['Skill1', 'Skill2', 'Skill3', 'Skill4', 'Skill5']
                    sk_dct = {}
                    for c in sc:
                        for skill in list(data3[c].values):
                            sk_dct[skill] = sk_dct.get(skill, 0) + 1
                    count = sk_dct.values()
                    sort_dct = sorted(
                        sk_dct.items(), key=lambda ele: ele[1], reverse=True)
                    sort_skill = [x[0] for x in sort_dct]
                    # print(sort_dct)
                    if max(count) < 5:
                        b = sort_skill[0:30]
                    else:
                        b = sort_skill[0:20]
                    d = [role] + readiness(b, sk_inp)
                    d1.append(d)
                    top_skill = b[0:10]
                    for sk in top_skill:
                        intermed.append([role, sk, 5])
                ready.append(d1)
                final.append(intermed)

        '''
        else:
            final = None
            senkey = None
        import json
        senkey = json.dumps(final)
        table = json.dumps(ready)
        '''
        template = loader.get_template('jinja2/results.html')
        return HttpResponse(template.render(request, {'sen': final, 'tab': ready, 'itertools': itertools, 'jsonify': jsonify}))
