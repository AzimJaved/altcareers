
import pandas as pd
from .settings import BASE_URL, BASE_DIR
data = pd.read_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_test.csv")

data_enc = data.copy()

s1 = list(set(list(data_enc['Skill1'].values)))
s2 = list(set(list(data_enc['Skill2'].values)))
s3 = list(set(list(data_enc['Skill3'].values)))
s4 = list(set(list(data_enc['Skill4'].values)))
s5 = list(set(list(data_enc['Skill5'].values)))

m = s1+s2+s3+s4+s5
skills = list(set(m))
skill_dct = {}
for i, val in enumerate(skills):
    skill_dct[val] = i


data_enc['Skill1'] = data_enc['Skill1'].replace(skill_dct)
data_enc['Skill2'] = data_enc['Skill2'].replace(skill_dct)
data_enc['Skill3'] = data_enc['Skill3'].replace(skill_dct)
data_enc['Skill4'] = data_enc['Skill4'].replace(skill_dct)
data_enc['Skill5'] = data_enc['Skill5'].replace(skill_dct)


rolecat = list(set(list(data_enc['Role Category'].values)))
rolcat_dct = {}
#set_rolecat = list(set(rolecat))
for i, val in enumerate(rolecat):
    rolcat_dct[val] = i
data_enc['Role Category'] = data_enc['Role Category'].replace(rolcat_dct)
role = list(set(list(data['Role'].values)))
role_dct = {}
for i, val in enumerate(role):
    role_dct[val] = i
data_enc['Role'] = data_enc['Role'].replace(role_dct)
#set_role = list(set(role))
fun = list(set(list(data['Functional Area'].values)))
fun_dct = {}
for i, val in enumerate(fun):
    fun_dct[val] = i
data_enc['Functional Area'] = data_enc['Functional Area'].replace(fun_dct)
#set_fun = list(set(fun))
industry = list(set(list(data['Industry'].values)))
ind_dct = {}
for i, val in enumerate(industry):
    ind_dct[val] = i
data_enc['Industry'] = data_enc['Industry'].replace(ind_dct)
#set_ind = list(set(industry))

#data.to_csv(BASE_DIR + "/Alt_Career/csv/job_dataset.csv", index=False, header=True)

data_enc.to_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_test_encoded.csv",
                index=False, header=True)
