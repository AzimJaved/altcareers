import pandas as pd

from .settings import BASE_URL, BASE_DIR
data = pd.read_csv(BASE_DIR + "/Alt_Career/csv/clean.csv")

for col in ['skill1', 'skill2', 'skill3', 'skill4', 'skill5']:
    n = []
    x = list(data[col].values)
    for item in x:
        item = item.strip().lstrip().rstrip()
        n.append(item)
    data[col.capitalize()] = n

data.drop(columns=['skill1', 'skill2', 'skill3', 'skill4',
                   'skill5', 'Key Skills'], axis=1, inplace=True)

data.rename(columns={'Role': 'Job Role',
                     'Role Category': 'Role'}, inplace=True)

data.rename(columns={'Job Role': 'Role Category'}, inplace=True)

data = data.drop(index=[1338, 11854, 13166, 29456])

data['Skill1'] = data['Skill1'].str.title()
data['Skill2'] = data['Skill2'].str.title()
data['Skill3'] = data['Skill3'].str.title()
data['Skill4'] = data['Skill4'].str.title()
data['Skill5'] = data['Skill5'].str.title()
data['Industry'] = data['Industry'].str.title()
data['Functional Area'] = data['Functional Area'].str.title()
data['Role Category'] = data['Role Category'].str.title()
data['Role'] = data['Role'].str.title()


data = data[data['Role Category'] != "Leading Logistics Firm"]
data = data[data['Role Category'] != "The Glove"]
data = data[data['Role Category'] != "Consulting"]
data = data[data['Role Category'] != "Aerial Telecom Solutions Pvt. Ltd."]
data = data[data['Role Category'] != "Https://Www.Artechinfo.In/"]
data = data[data['Role Category'] != "Oyo Rooms"]
data = data[data['Role Category'] != "Csr & Sustainability"]

data = data[data['Role Category'] != "Hiring For Logistics Company"]
data = data[data['Role Category'] != "Beauty Services"]
data = data[data['Role Category'] !=
            "Quality Assurance & Quality Control-Compliance & Regulatory"]
data = data[data['Role Category'] != "Aerial Telecom Solutions Pvt. Ltd."]
data = data[data['Role Category'] != "Hotel Services"]


sk_col = ['Skill1', 'Skill2', 'Skill3', 'Skill4', 'Skill5']
count = 0
for ind, row in data.iterrows():

    l = []
    for i in range(len(sk_col)):
        l.append(row[sk_col[i]])
    if len(list(set(l))) < 5:
        data.drop(ind, inplace=True)
    else:
        pass

data['Functional Area'] = data['Functional Area'].replace(
    'Beauty/Fitness/Spa Services', 'Beauty / Fitness / Spa Services')

data['Industry'] = data['Industry'].replace(['Accounting / Finance', 'Advertising / Pr / Mr / Event Management', 'Agriculture / Dairy', 'Automobile / Auto Anciliary / Auto Components', 'Aviation / Aerospace Firms', 'Banking / Financial Services / Broking', 'Bpo / Call Centre / Ites', 'Chemicals / Petrochemical / Plastic / Rubber', 'Construction / Engineering / Cement / Metals', 'Consumer Electronics / Appliances / Durables', 'Courier / Transportation / Freight / Warehousing', 'Education / Teaching / Training', 'Fmcg / Foods / Beverage', 'Gems / Jewellery', 'Glass / Glassware', 'Heat Ventilation / Air Conditioning', 'Industrial Products / Heavy Machinery', 'Internet / Ecommerce', 'It-Software / Software Services', 'Kpo / Research / Analytics', 'Media / Entertainment / Internet', 'Medical / Healthcare / Hospitals', 'Mining / Quarrying', 'Ngo / Social Services / Regulators / Industry Associations', 'Oil And Gas / Energy / Power / Infrastructure', 'Pharma / Biotech / Clinical Research', 'Real Estate / Property', 'Recruitment / Staffing', 'Retail / Wholesale', 'Semiconductors / Electronics', 'Strategy / Management Consulting Firms', 'Telecom / Isp', 'Textiles / Garments / Accessories',
                                             'Travel / Hotels / Restaurants / Airlines / Railways'], ['Accounting, Finance', 'Advertising, Pr, Mr, Event Management', 'Agriculture, Dairy', 'Automobile, Auto Anciliary, Auto Components', 'Aviation, Aerospace, Aeronautical', 'Banking, Financial Services, Broking', 'Bpo, Call Centre, Ites', 'Chemicals, Petrochemical, Plastic, Rubber', 'Construction, Engineering, Cement, Metals', 'Consumer Electronics, Appliances, Durables', 'Courier, Transportation, Freight , Warehousing', 'Education, Teaching, Training', 'Fmcg, Foods, Beverage', 'Gems, Jewellery', 'Glass, Glassware', 'Heat Ventilation, Air Conditioning', 'Industrial Products, Heavy Machinery', 'Internet, Ecommerce', 'It-Software, Software Services', 'Kpo, Research, Analytics', 'Media, Entertainment, Internet', 'Medical, Healthcare, Hospitals', 'Mining, Quarrying', 'Ngo, Social Services, Regulators, Industry Associations', 'Oil And Gas, Energy, Power, Infrastructure', 'Pharma, Biotech, Clinical Research', 'Real Estate, Property', 'Recruitment, Staffing', 'Retail, Wholesale', 'Semiconductors, Electronics', 'Strategy, Management Consulting Firms', 'Telcom, Isp', 'Textiles, Garments, Accessories', 'Travel , Hotels , Restaurants , Airlines , Railways'])

'''
sk_col = ['Skill1', 'Skill2', 'Skill3', 'Skill4', 'Skill5']
s1 = list(data['Skill1'].values)
s2 = list(data['Skill2'].values)
s3 = list(data['Skill3'].values)
s4 = list(data['Skill4'].values)
s5 = list(data['Skill5'].values)

m = s1+s2+s3+s4+s5
set_m = list(set(m))
l = [i for i in range(len(set_m))]
skill_map = dict(zip(set_m,l))


index = []
for j in range(4):
    set1 = set(m[j])
    for k in range(j+1,5):
        set2 = set(m[k])
        s = list(set1 & set2)
        #print(len(s))
        index_names = data[data['Skill{}'.format(k+1)].isin(s)].index
        index.extend(index_names)
        #print(len(set(s1) & (set(s2))))
index = list(set(index))
index.sort(reverse=True)
if len(index)>0:
    data.drop(index, axis = 0, inplace=True)

    for i in m[k]:
        for j in range(k+1,5):
            if i in m[j]:
                ind = m[j].index(i)
                ind = df[ (df['Skill{}'.format(j+1)] == i).index
                #if m[k][ind] != m[j][ind]:
                #    m[k][ind], m[j][ind] = m[j][ind], m[k][ind]


data.drop(sk_col, axis=1, inplace=True)
data['Skill1'] = m[0]
data['Skill2'] = m[1]
data['Skill3'] = m[2]
data['Skill4'] = m[3]
data['Skill5'] = m[4]

set1 = set(s1)
set2 = set(s2)
s = list(set1 & set2)
print(len(s))
for ind, sk2 in enumerate(s2):
    if (sk2 in s) and (s1[ind] != sk2):
        s1[ind], s2[ind] = s2[ind], s1[ind]
print(len(set(s1) & (set(s2))))
'''

data2 = data[data['Role Category'] == 'Programming & Design']
data2 = data2.iloc[::2]
ind = list(data2.index.values)

data.drop(ind, inplace=True)

for rc in list(set(list(data['Role Category'].values))):
    data2 = data[data['Role Category'] == rc]
    l = len(data2)
    if l < 100:
        data = data.append([data2]*5, ignore_index=False)
    elif l > 100 and l < 500:
        data = data.append([data2]*3, ignore_index=False)

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

data.to_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_test.csv", index=False, header=True)

data_enc.to_csv(BASE_DIR + "/Alt_Career/csv/job_dataset_test_encoded.csv",
                index=False, header=True)
