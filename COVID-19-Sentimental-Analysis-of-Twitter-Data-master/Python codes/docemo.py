import json
import csv
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from ibm_watson import NaturalLanguageUnderstandingV1
#An IBM CLOUD SERVICE
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, CategoriesOptions, ConceptsOptions, EmotionOptions, RelationsOptions, SemanticRolesOptions, SentimentOptions


def Convert(a):
    it = iter(listofTuples)
    res_dct = dict(zip(it, it))
    return res_dct

authenticator = IAMAuthenticator('mKzR3k6BF2W3tMUmoX3_Xvxze4LL0-f_q8FM5QMsFIFY')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator
)
from ibm_watson import IAMTokenManager

iam_token_manager = IAMTokenManager(apikey='mKzR3k6BF2W3tMUmoX3_Xvxze4LL0-f_q8FM5QMsFIFY')
token = iam_token_manager.get_token()

from ibm_cloud_sdk_core.authenticators import BearerTokenAuthenticator

# in the constructor, assuming control of managing the token
authenticator1 = BearerTokenAuthenticator(token)
natural_language_understanding1 = NaturalLanguageUnderstandingV1(version='2019-07-12',
                        authenticator=authenticator1)
natural_language_understanding.set_service_url(
            'https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/c70c1850-5873-495c-b449-d84d30415f06')
natural_language_understanding.set_disable_ssl_verification(True)
def listtostring(s):
    str1 = " "
    return (str1.join(s))
cn=cp=cng=e1=e2=e3=e4=e5=0
f_name = input("enter file in csv format")
with open("C:\\Users\\HP\\Desktop\\"+f_name+".csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        j = 0
        row = listtostring(row)
        response = natural_language_understanding.analyze(
            text=row,
            language='en',
            features=Features(
                sentiment=SentimentOptions(),
                emotion=EmotionOptions(),
            )).get_result()

        sen1 = response.get('sentiment').get('document').get('score')
        sen2 = response.get('sentiment').get('document').get('label')
        if sen1 == 0:
            cn += 1

        elif sen1 > 0:
            cp += 1

        else:
            cng += 1
        op = response.get('emotion').get('document').get('emotion')
        #print(type(op))
        # Create a list of tuples sorted by index 1 i.e. value field
        listofTuples = sorted(op.items(), reverse=True, key=lambda x: x[1])
        ll = listofTuples[0]
        d = dict(listofTuples)
        for k,v in d.items():
            d1 = k
            d2 = v
            j += 1
            if j > 0:
                break
        if d1 == 'sadness':
            e1 += 1
        elif d1 == 'joy':
            e2 += 1
        elif d1 == 'fear':
            e3 += 1
        elif d1 == 'disgust':
            e4 += 1
        else:
            e5 += 1

        #print(i, sen1, sen2, d1, d2)

s = s1 = 0
s = cn + cng + cp
pp = (cp * 100) / s
ngp = (cng * 100) / s
np = (cn * 100) / s
s1 = e1+e2+e3+e4+e5
e1p = (e1 * 100) / s1
e2p = (e2 * 100) / s1
e3p = (e3 * 100) / s1
e4p = (e4 * 100) / s1
e5p = (e5 * 100) / s1
print(np, pp, ngp, e1p, e2p, e3p, e4p, e5p)
'''''
with open('C:\\Users\\HP\\Desktop\\docemo.csv', 'a', newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerow([f_name, np, pp, ngp, e1p, e2p, e3p, e4p, e5p])
'''
with open('C:\\Users\\HP\\Desktop\\;lockdownrx_1.csv', 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(['doc','neu%','pos%','neg%','sadness%','joy%','fear%','disgust%','anger%'])
    writer.writerow([f_name, round(np, 2), round(pp, 2), round(ngp, 2), round(e1p, 2),round(e2p, 2),round(e3p, 2),round(e4p, 2),round(e5p, 2)])