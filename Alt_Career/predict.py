import pandas as pd
import os
import pickle
from .dataprep import ind_dct, fun_dct, skill_dct, rolcat_dct, role_dct

forest = pickle.load(open(BASE_DIR + "/Alt_Career/csv/model.pkl",'rb'))



def predict(ind,f_area,sk1,sk2,sk3,sk4,sk5,ind_,f_area_,sk1_,sk2_,sk3_,sk4_,sk5_):
    data = pd.read_csv(BASE_DIR + '/Alt_Career/csv/job_dataset.csv')
    data_enc = pd.read_csv(BASE_DIR + '/Alt_Career/csv/job_dataset_encoded.csv')
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
                data2 = data[(data['Role Category'] == rol_cat) & (data['Industry'] != ind_)]
                #display(data2)
                print(set(data2['Industry'].values))
                ind_lt = list(set(data2['Industry'].values))
                role_lt = []
                d1 = []
                                    
                for i in ind_lt:
                    intermed = []
                    intermed.append([rol_cat,i,3])
                    data3 = data2[data2['Industry'] == i]
                    role_lt = list(set(list(data3['Role'].values)))
                    for role in role_lt:
                        intermed.append([i, role, 3])
                    for role in role_lt :
                        data4 = data3[data3['Role'] == role]
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
                        d = [i,role] + readiness(b, sk_inp)
                        d1.append(d)
                        top_skill = b[0:5]
                        for sk in top_skill:
                            unique = " " + str(sk) + " "
                            intermed.append([role, unique, 3])
                    final.append(intermed)
                ready.append(d1)
                

        '''
        else:
            final = None
            senkey = None
        import json
        senkey = json.dumps(final)
        table = json.dumps(ready)
        '''
        return ready,final
